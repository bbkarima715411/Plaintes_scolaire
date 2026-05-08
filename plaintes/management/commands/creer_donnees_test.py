from django.core.management.base import BaseCommand

from plaintes.models import Plainte


class Command(BaseCommand):
    help = 'Crée des plaintes fictives pour tester l’application.'

    def handle(self, *args, **options):
        plaintes = [
            {
                'numero_dossier': 'DOS-2026-001',
                'numero_fase': 'FASE-1001',
                'canal_utilise': 'Courrier',
                'nom_ecole': 'École communale du Centre',
                'lieu_ecole': 'Bruxelles',
                'nom_parent': 'Dupont',
                'prenom_parent': 'Marie',
                'nom_enfant': 'Dupont',
                'prenom_enfant': 'Lucas',
                'genre_enfant': Plainte.GENRE_MASCULIN,
                'personnel_concerne': 'Direction',
                'motif_plainte': 'Plainte concernant le suivi administratif du dossier.',
                'personne_traitant_dossier': 'Karima',
                'statut': Plainte.STATUT_NOUVELLE,
                'retour_wf_signe': False,
                'remarque': 'Dossier fictif pour test.',
            },
            {
                'numero_dossier': 'DOS-2026-002',
                'numero_fase': 'FASE-1002',
                'canal_utilise': 'Email',
                'nom_ecole': 'Institut Saint-Pierre',
                'lieu_ecole': 'Liège',
                'nom_parent': 'Martin',
                'prenom_parent': 'Sophie',
                'nom_enfant': 'Martin',
                'prenom_enfant': 'Emma',
                'genre_enfant': Plainte.GENRE_FEMININ,
                'personnel_concerne': 'Enseignant',
                'motif_plainte': 'Plainte concernant une communication insuffisante avec les parents.',
                'personne_traitant_dossier': 'Karima',
                'statut': Plainte.STATUT_EN_COURS,
                'retour_wf_signe': True,
                'remarque': 'À vérifier avec la direction.',
            },
            {
                'numero_dossier': 'DOS-2026-003',
                'numero_fase': 'FASE-1003',
                'canal_utilise': 'Téléphone',
                'nom_ecole': 'Athénée Royal Nord',
                'lieu_ecole': 'Namur',
                'nom_parent': 'Bernard',
                'prenom_parent': 'Ahmed',
                'nom_enfant': 'Bernard',
                'prenom_enfant': 'Nora',
                'genre_enfant': Plainte.GENRE_FEMININ,
                'personnel_concerne': 'Éducateur',
                'motif_plainte': 'Plainte concernant un incident survenu pendant la récréation.',
                'personne_traitant_dossier': 'Karima',
                'statut': Plainte.STATUT_EN_ATTENTE,
                'retour_wf_signe': False,
                'remarque': 'Attente de documents complémentaires.',
            },
            {
                'numero_dossier': 'DOS-2026-004',
                'numero_fase': 'FASE-1004',
                'canal_utilise': 'Courrier',
                'nom_ecole': 'École Les Tilleuls',
                'lieu_ecole': 'Charleroi',
                'nom_parent': 'Lambert',
                'prenom_parent': 'Claire',
                'nom_enfant': 'Lambert',
                'prenom_enfant': 'Hugo',
                'genre_enfant': Plainte.GENRE_MASCULIN,
                'personnel_concerne': 'Secrétariat',
                'motif_plainte': 'Plainte relative à une erreur dans un document scolaire.',
                'personne_traitant_dossier': 'Karima',
                'statut': Plainte.STATUT_TRAITEE,
                'retour_wf_signe': True,
                'remarque': 'Dossier traité.',
            },
            {
                'numero_dossier': 'DOS-2026-005',
                'numero_fase': 'FASE-1005',
                'canal_utilise': 'Guichet',
                'nom_ecole': 'Collège Sainte-Marie',
                'lieu_ecole': 'Mons',
                'nom_parent': 'Petit',
                'prenom_parent': 'Nadia',
                'nom_enfant': 'Petit',
                'prenom_enfant': 'Yanis',
                'genre_enfant': Plainte.GENRE_MASCULIN,
                'personnel_concerne': 'Direction',
                'motif_plainte': 'Plainte concernant le délai de réponse à une demande parentale.',
                'personne_traitant_dossier': 'Karima',
                'statut': Plainte.STATUT_ARCHIVEE,
                'retour_wf_signe': True,
                'remarque': 'Archive fictive.',
            },
        ]

        compteur = 0
        for plainte in plaintes:
            objet, cree = Plainte.objects.get_or_create(
                numero_dossier=plainte['numero_dossier'],
                defaults=plainte,
            )
            if cree:
                compteur += 1

        self.stdout.write(self.style.SUCCESS(f'{compteur} plainte(s) fictive(s) créée(s).'))
