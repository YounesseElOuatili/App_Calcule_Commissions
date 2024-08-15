from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import VendeurAgricole, VendeurPdv, PalierAgricole, PalierPdv
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def calcul_commissions(request):
    # Choisir les vendeurs en fonction du type (Agricole ou PDV)
    vendeur_type = request.GET.get('vendeur_type', 'agricole')  # default to 'agricole'
    
    if vendeur_type == 'pdv':
        vendeurs = VendeurPdv.objects.all()
        default_commissions = [0.4, 0.5, 0.7, 0.7, 0.8, 0.9]
    else:
        vendeurs = VendeurAgricole.objects.all()
        default_commissions = [0.25, 0.5, 0.5, 0.7, 0.8, 0.9]
    
    total = 0
    paliers_results = {}
    form_data = {
        'valeur': '',
        'date': '',
        'paliers': {i: {'min': '', 'max': '', 'com': ''} for i in range(1, 7)}
    }

    # Default paliers values
    default_paliers = {
        1: {'min': 0, 'max': 2000, 'com': default_commissions[0]},
        2: {'min': 2000, 'max': 3000, 'com': default_commissions[1]},
        3: {'min': 3000, 'max': 4000, 'com': default_commissions[2]},
        4: {'min': 4000, 'max': 5000, 'com': default_commissions[3]},
        5: {'min': 5000, 'max': 8000, 'com': default_commissions[4]},
        6: {'min': 8000, 'max': 20000, 'com': default_commissions[5]}
    }

    if request.method == 'POST':
        val = request.POST.get('valeur')
        date = request.POST.get('date')
        if val and date:
            form_data['valeur'] = val
            form_data['date'] = date
            val = float(val)

            for i in range(1, 7):
                pal_min = request.POST.get(f'palMin{i}', '')
                pal_max = request.POST.get(f'palMax{i}', '')
                com = request.POST.get(f'com{i}', '')

                form_data['paliers'][i] = {
                    'min': pal_min,
                    'max': pal_max,
                    'com': com
                }

                if pal_min and pal_max and com:
                    pal_min = float(pal_min)
                    pal_max = float(pal_max)
                    com = float(com)

                    result = 0
                    if pal_min <= val < pal_max:
                        result = (val - pal_min) * com
                    elif val >= pal_max:
                        result = (pal_max - pal_min) * com

                    total += result
                    paliers_results[i] = result

            # Save the palier to the database if 'btnValid' was clicked
            if 'btnValid' in request.POST:
                selected_vendeur_id = request.POST.get('combUtil')
                if selected_vendeur_id:
                    try:
                        if vendeur_type == 'pdv':
                            selected_vendeur = VendeurPdv.objects.get(external_id_v=selected_vendeur_id)
                            new_palier = PalierPdv
                        else:
                            selected_vendeur = VendeurAgricole.objects.get(external_id_v=selected_vendeur_id)
                            new_palier = PalierAgricole

                        new_palier_instance = new_palier(
                            external_id=f'PAL-{timezone.now().strftime("%Y%m%d%H%M%S")}',  # Unique ID
                            vendeur=selected_vendeur,
                            qte=form_data['valeur'],
                            total=total,
                            date=date  # Stocke la date choisie
                        )
                        new_palier_instance.save()
                    except (VendeurAgricole.DoesNotExist, VendeurPdv.DoesNotExist):
                        return HttpResponse("Vendeur non trouvé")

    return render(request, 'calcul_commissions.html', {
        'vendeurs': vendeurs,
        'default_paliers': default_paliers,
        'paliers_results': paliers_results,
        'form_data': form_data,
        'total': total,
        'vendeur_type': vendeur_type
    })


from django.shortcuts import render
from django.utils import timezone
from .models import PalierAgricole, PalierPdv

def tableau_paliers(request):
    vendeur_type = request.GET.get('vendeur_type', 'agricole')  # default to 'agricole'
    date = request.GET.get('date', timezone.now().date())
    total_dh = 0  # Initialize the total amount

    # Filtrer les paliers en fonction du type de vendeur et de la date
    if vendeur_type == 'pdv':
        paliers = PalierPdv.objects.filter(date=date)
    else:
        paliers = PalierAgricole.objects.filter(date=date)

    # Calculer le total des montants
    total_dh = sum(palier.total for palier in paliers)

    # Rendre le template avec les données nécessaires
    return render(request, 'tableau_paliers.html', {
        'paliers': paliers,
        'vendeur_type': vendeur_type,
        'date': date,
        'total_dh': total_dh,  # Pass the total amount to the template
    })

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import PalierPdv, PalierAgricole
from datetime import datetime

def export_pdf(request):
    vendeur_type = request.GET.get('vendeur_type')
    date_str = request.GET.get('date')

    # Convertir la chaîne de date en objet datetime si elle existe
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            date_formatted = date.strftime('%d%m%Y')  # Format de la date pour le nom du fichier
        except ValueError:
            return HttpResponse("Date invalide.", status=400)
    else:
        return HttpResponse("Date non spécifiée.", status=400)

    # Sélectionner le modèle approprié en fonction du type de vendeur
    if vendeur_type == 'agricole':
        paliers = PalierAgricole.objects.filter(date=date)
    elif vendeur_type == 'pdv':
        paliers = PalierPdv.objects.filter(date=date)
    else:
        return HttpResponse("Type de vendeur non valide.", status=400)

    # Calculer le total des commissions
    total_dh = sum(palier.total for palier in paliers)

    context = {
        'paliers': paliers,
        'vendeur_type': vendeur_type,
        'date': date,
        'total_dh': total_dh,  # Passer le total des commissions au template
    }

    # Utilisez le chemin du template correct
    template = get_template('template_pdf.html')
    html = template.render(context)

    # Créer un nom de fichier basé sur la date choisie
    file_name = f"palier_{date_formatted}.pdf"

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Créer le PDF en utilisant xhtml2pdf
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)

    if pisa_status.err:
        return HttpResponse('Erreur de génération du PDF.', status=500)

    return response

from django.shortcuts import render

def profile(request):
    return render(request, 'tableau_paliers.html')
