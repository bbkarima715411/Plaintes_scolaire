from django import forms

from .models import Plainte


class PlainteForm(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = [
            'canal_utilise',
            'date_courrier',
            'numero_dossier',
            'numero_fase',
            'nom_ecole',
            'lieu_ecole',
            'nom_parent',
            'prenom_parent',
            'nom_enfant',
            'prenom_enfant',
            'genre_enfant',
            'personnel_concerne',
            'motif_plainte',
            'personne_traitant_dossier',
            'statut',
            'retour_wf_signe',
            'remarque',
        ]
        widgets = {
            'date_courrier': forms.DateInput(attrs={'type': 'date'}),
            'motif_plainte': forms.Textarea(attrs={'rows': 4}),
            'remarque': forms.Textarea(attrs={'rows': 3}),
        }
