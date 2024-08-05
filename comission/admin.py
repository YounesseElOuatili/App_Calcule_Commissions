from django.contrib import admin
from .models import PalierAgricole, PalierPdv, VendeurAgricole, VendeurPdv

@admin.register(PalierAgricole)
class PalierAgricoleAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'vendeur', 'qte', 'total', 'date')
    search_fields = ('external_id', 'date')
    list_filter = ('date',)
    ordering = ('external_id',)

@admin.register(PalierPdv)
class PalierPdvAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'vendeur', 'qte', 'total', 'date')
    search_fields = ('external_id', 'date')
    list_filter = ('date',)
    ordering = ('external_id',)

@admin.register(VendeurAgricole)
class VendeurAgricoleAdmin(admin.ModelAdmin):
    list_display = ('external_id_v', 'nom')
    search_fields = ('external_id_v', 'nom')
    ordering = ('external_id_v',)

@admin.register(VendeurPdv)
class VendeurPdvAdmin(admin.ModelAdmin):
    list_display = ('external_id_v', 'nom')
    search_fields = ('external_id_v', 'nom')
    ordering = ('external_id_v',)
