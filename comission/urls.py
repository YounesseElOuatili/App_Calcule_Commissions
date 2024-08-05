# comission/urls.py
from django.urls import path
from . import views

app_name = 'comission'

urlpatterns = [
    # Ajoutez vos routes ici
    
    path('calcul_commissions/', views.calcul_commissions, name='calcul_commissions'),
    path('tableau_paliers/', views.tableau_paliers, name='tableau_paliers'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
    path('accounts/profile/', views.profile, name='profile'),
    # Autres routes
]
