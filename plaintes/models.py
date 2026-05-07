from django.db import models


class Plainte(models.Model):
    STATUT_NOUVELLE = 'nouvelle'
    STATUT_EN_COURS = 'en_cours'
    STATUT_EN_ATTENTE = 'en_attente'
    STATUT_TRAITEE = 'traitee'
    STATUT_ARCHIVEE = 'archivee'

    STATUT_CHOICES = [
        (STATUT_NOUVELLE, 'Nouvelle'),
        (STATUT_EN_COURS, 'En cours'),
        (STATUT_EN_ATTENTE, 'En attente'),
        (STATUT_TRAITEE, 'Traitée'),
        (STATUT_ARCHIVEE, 'Archivée'),
    ]

    GENRE_MASCULIN = 'masculin'
    GENRE_FEMININ = 'feminin'
    GENRE_AUTRE = 'autre'

    GENRE_CHOICES = [
        (GENRE_MASCULIN, 'Masculin'),
        (GENRE_FEMININ, 'Féminin'),
        (GENRE_AUTRE, 'Autre'),
    ]

    canal_utilise = models.CharField(max_length=100, blank=True)
    date_courrier = models.DateField(null=True, blank=True)
    numero_dossier = models.CharField(max_length=100, unique=True)
    numero_fase = models.CharField(max_length=100, blank=True)
    nom_ecole = models.CharField(max_length=255)
    lieu_ecole = models.CharField(max_length=255, blank=True)
    nom_parent = models.CharField(max_length=150)
    prenom_parent = models.CharField(max_length=150, blank=True)
    nom_enfant = models.CharField(max_length=150, blank=True)
    prenom_enfant = models.CharField(max_length=150, blank=True)
    genre_enfant = models.CharField(max_length=20, choices=GENRE_CHOICES, blank=True)
    personnel_concerne = models.CharField(max_length=255, blank=True)
    motif_plainte = models.TextField()
    personne_traitant_dossier = models.CharField(max_length=150, blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default=STATUT_NOUVELLE)
    retour_wf_signe = models.BooleanField(default=False)
    remarque = models.TextField(blank=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    modifie_le = models.DateTimeField(auto_now=True)
    modifie_par = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-cree_le']
        verbose_name = 'Plainte'
        verbose_name_plural = 'Plaintes'

    def __str__(self):
        return f'{self.numero_dossier} - {self.nom_ecole}'
