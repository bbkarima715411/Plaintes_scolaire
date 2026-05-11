from django.db import models


class Plainte(models.Model):
    class Statut(models.TextChoices):
        NOUVELLE = 'nouvelle', 'Nouvelle'
        EN_COURS = 'en_cours', 'En cours'
        EN_ATTENTE = 'en_attente', 'En attente'
        TRAITEE = 'traitee', 'Traitée'
        ARCHIVEE = 'archivee', 'Archivée'

    class Genre(models.TextChoices):
        MASCULIN = 'masculin', 'Masculin'
        FEMININ = 'feminin', 'Féminin'
        AUTRE = 'autre', 'Autre'

    canal_utilise = models.CharField(max_length=100, blank=True)
    date_courrier = models.DateField(null=True, blank=True)
    numero_dossier = models.CharField(max_length=100, unique=True)
    numero_fase = models.CharField(max_length=100, blank=True)
    nom_ecole = models.CharField(max_length=255)
    lieu_ecole = models.CharField(max_length=255, blank=True)
    nom_parent = models.CharField(max_length=150)
    prenom_parent = models.CharField(max_length=150, blank=True)
    nom_masculin = models.CharField(max_length=150, blank=True)
    nom_feminin = models.CharField(max_length=150, blank=True)
    nom_enfant = models.CharField(max_length=150, blank=True)
    prenom_enfant = models.CharField(max_length=150, blank=True)
    genre_enfant = models.CharField(max_length=20, choices=Genre.choices, blank=True)
    personnel_concerne = models.CharField(max_length=255, blank=True)
    motif_plainte = models.TextField()
    personne_traitant_dossier = models.CharField(max_length=150, blank=True)
    statut = models.CharField(max_length=20, choices=Statut.choices, default=Statut.NOUVELLE)
    retour_wf_signe = models.BooleanField(default=False)
    retour_wf_signe_le = models.DateField(null=True, blank=True)
    conclusion = models.TextField(blank=True)
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
