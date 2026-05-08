from django.contrib import admin

from .models import Plainte


@admin.register(Plainte)
class PlainteAdmin(admin.ModelAdmin):
    list_display = (
        'numero_dossier',
        'nom_ecole',
        'nom_parent',
        'statut',
        'date_courrier',
        'modifie_le',
    )
    list_filter = ('statut', 'retour_wf_signe', 'date_courrier')
    search_fields = (
        'numero_dossier',
        'numero_fase',
        'nom_ecole',
        'nom_parent',
        'prenom_parent',
        'prenom_enfant',
    )
    readonly_fields = ('cree_le', 'modifie_le')
