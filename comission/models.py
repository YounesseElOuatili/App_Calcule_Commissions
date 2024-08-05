from django.db import models

# Modèle pour les vendeurs agricoles
class VendeurAgricole(models.Model):
    external_id_v = models.CharField(max_length=20, primary_key=True, verbose_name="Référence")
    nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom du Vendeur")

    class Meta:
        ordering = ["external_id_v"]
        verbose_name = "Vendeur Agricole"
        db_table = "vendeur_agricole"

    def __str__(self):
        return self.nom

# Modèle pour les vendeurs PDV
class VendeurPdv(models.Model):
    external_id_v = models.CharField(max_length=20, primary_key=True, verbose_name="Référence")
    nom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom du Vendeur")

    class Meta:
        ordering = ["external_id_v"]
        verbose_name = "Vendeur PDV"
        db_table = "vendeur_pdv"

    def __str__(self):
        return self.nom

# Modèle pour les paliers agricoles
class PalierAgricole(models.Model):
    external_id = models.CharField(max_length=20, primary_key=True, verbose_name="Référence")
    qte = models.IntegerField(null=True, blank=True, verbose_name="Quantité")
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Total")
    date = models.DateField(null=True, blank=True, verbose_name="Date")
    vendeur = models.ForeignKey('VendeurAgricole', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Vendeur")

    class Meta:
        ordering = ["external_id"]
        verbose_name = "Palier Agricole"
        db_table = "palier_agricole"

    def __str__(self):
        return f"Palier de {self.total} le {self.date}"

# Modèle pour les paliers PDV
class PalierPdv(models.Model):
    external_id = models.CharField(max_length=20, primary_key=True, verbose_name="Référence")
    qte = models.IntegerField(null=True, blank=True, verbose_name="Quantité")
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Total")
    date = models.DateField(null=True, blank=True, verbose_name="Date")
    vendeur = models.ForeignKey('VendeurPdv', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Vendeur")

    class Meta:
        ordering = ["external_id"]
        verbose_name = "Palier PDV"
        db_table = "palier_pdv"

    def __str__(self):
        return f"Palier de {self.total} le {self.date}"
