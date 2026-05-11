from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from openpyxl import Workbook

from .forms import PlainteForm
from .models import Plainte


def identification_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('nom_utilisateur'):
            return redirect('identification')
        return view_func(request, *args, **kwargs)
    return wrapper


def identification(request):
    if request.method == 'POST':
        nom_utilisateur = request.POST.get('nom_utilisateur', '').strip()
        if nom_utilisateur:
            request.session['nom_utilisateur'] = nom_utilisateur
            return redirect('plainte_list')

    return render(request, 'plaintes/identification.html')


def changer_utilisateur(request):
    request.session.pop('nom_utilisateur', None)
    return redirect('identification')


@login_required
@identification_required
def plainte_list(request):
    recherche = request.GET.get('recherche', '')
    statut = request.GET.get('statut', '')
    plaintes = Plainte.objects.all()

    if recherche:
        for mot in recherche.split():
            plaintes = plaintes.filter(
                Q(numero_dossier__icontains=mot)
                | Q(numero_fase__icontains=mot)
                | Q(nom_ecole__icontains=mot)
                | Q(nom_parent__icontains=mot)
                | Q(prenom_parent__icontains=mot)
                | Q(nom_enfant__icontains=mot)
                | Q(prenom_enfant__icontains=mot)
            )

    if statut:
        plaintes = plaintes.filter(statut=statut)

    return render(request, 'plaintes/plainte_list.html', {
        'plaintes': plaintes,
        'recherche': recherche,
        'statut': statut,
        'statut_choices': Plainte.STATUT_CHOICES,
    })


@login_required
@identification_required
def plainte_export_excel(request):
    recherche = request.GET.get('recherche', '')
    statut = request.GET.get('statut', '')
    plaintes = Plainte.objects.all()

    if recherche:
        for mot in recherche.split():
            plaintes = plaintes.filter(
                Q(numero_dossier__icontains=mot)
                | Q(numero_fase__icontains=mot)
                | Q(nom_ecole__icontains=mot)
                | Q(nom_parent__icontains=mot)
                | Q(prenom_parent__icontains=mot)
                | Q(nom_enfant__icontains=mot)
                | Q(prenom_enfant__icontains=mot)
            )

    if statut:
        plaintes = plaintes.filter(statut=statut)

    workbook = Workbook()
    feuille = workbook.active
    feuille.title = 'Plaintes'

    entetes = [
        'Canal utilisé',
        'Date du courrier',
        'Numéro de dossier',
        'Numéro FASE',
        'Nom de l’école',
        'Lieu de l’école',
        'Nom du parent',
        'Prénom du parent',
        'Nom de l’enfant',
        'Prénom de l’enfant',
        'Genre enfant',
        'Personnel concerné',
        'Motif de la plainte',
        'Personne traitant le dossier',
        'Statut',
        'Retour WF signé',
        'Remarque',
        'Créée le',
        'Modifiée le',
    ]
    feuille.append(entetes)

    for plainte in plaintes:
        feuille.append([
            plainte.canal_utilise,
            plainte.date_courrier.strftime('%d/%m/%Y') if plainte.date_courrier else '',
            plainte.numero_dossier,
            plainte.numero_fase,
            plainte.nom_ecole,
            plainte.lieu_ecole,
            plainte.nom_parent,
            plainte.prenom_parent,
            plainte.nom_enfant,
            plainte.prenom_enfant,
            plainte.get_genre_enfant_display(),
            plainte.personnel_concerne,
            plainte.motif_plainte,
            plainte.personne_traitant_dossier,
            plainte.get_statut_display(),
            'Oui' if plainte.retour_wf_signe else 'Non',
            plainte.remarque,
            plainte.cree_le.strftime('%d/%m/%Y %H:%M') if plainte.cree_le else '',
            plainte.modifie_le.strftime('%d/%m/%Y %H:%M') if plainte.modifie_le else '',
        ])

    fichier = BytesIO()
    workbook.save(fichier)
    fichier.seek(0)

    response = HttpResponse(
        fichier.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename="plaintes_selectionnees.xlsx"'
    return response


@login_required
@identification_required
def plainte_detail(request, pk):
    plainte = get_object_or_404(Plainte, pk=pk)
    return render(request, 'plaintes/plainte_detail.html', {'plainte': plainte})


@login_required
@identification_required
def plainte_create(request):
    if request.method == 'POST':
        form = PlainteForm(request.POST)
        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.modifie_par = request.user
            plainte.save()
            return redirect('plainte_detail', pk=plainte.pk)
    else:
        form = PlainteForm(initial={
            'personne_traitant_dossier': request.session.get('nom_utilisateur', ''),
        })

    return render(request, 'plaintes/plainte_form.html', {'form': form, 'titre': 'Ajouter une plainte'})


@login_required
@identification_required
def plainte_update(request, pk):
    plainte = get_object_or_404(Plainte, pk=pk)

    if request.method == 'POST':
        form = PlainteForm(request.POST, instance=plainte)
        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.modifie_par = request.user
            plainte.save()
            return redirect('plainte_detail', pk=plainte.pk)
    else:
        form = PlainteForm(instance=plainte)

    return render(request, 'plaintes/plainte_form.html', {'form': form, 'titre': 'Modifier une plainte'})


@login_required
@identification_required
def plainte_delete(request, pk):
    plainte = get_object_or_404(Plainte, pk=pk)

    if request.method == 'POST':
        plainte.delete()
        return redirect('plainte_list')

    return render(request, 'plaintes/plainte_confirm_delete.html', {'plainte': plainte})
