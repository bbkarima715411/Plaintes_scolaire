from django import forms

from .models import Plainte


class PlainteForm(forms.ModelForm):
    retour_wf_signe = forms.TypedChoiceField(
        choices=((True, 'Oui'), (False, 'Non')),
        coerce=lambda value: value == 'True',
        widget=forms.Select,
        label='Retour wf signé',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

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
            'nom_masculin',
            'nom_feminin',
            'nom_enfant',
            'prenom_enfant',
            'genre_enfant',
            'personnel_concerne',
            'motif_plainte',
            'personne_traitant_dossier',
            'statut',
            'retour_wf_signe',
            'retour_wf_signe_le',
            'conclusion',
            'remarque',
        ]
        widgets = {
            'date_courrier': forms.DateInput(attrs={'type': 'date'}),
            'retour_wf_signe_le': forms.DateInput(attrs={'type': 'date'}),
            'genre_enfant': forms.Select(),
            'statut': forms.Select(),
            'motif_plainte': forms.Textarea(attrs={'rows': 4}),
            'conclusion': forms.Textarea(attrs={'rows': 3}),
            'remarque': forms.Textarea(attrs={'rows': 3}),
        }
