from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlainteForm
from .models import Plainte


@login_required
def dashboard(request):
    total_plaintes = Plainte.objects.count()
    plaintes_en_cours = Plainte.objects.filter(statut=Plainte.STATUT_EN_COURS).count()
    plaintes_traitees = Plainte.objects.filter(statut=Plainte.STATUT_TRAITEE).count()
    dernieres_plaintes = Plainte.objects.all()[:5]

    return render(request, 'plaintes/dashboard.html', {
        'total_plaintes': total_plaintes,
        'plaintes_en_cours': plaintes_en_cours,
        'plaintes_traitees': plaintes_traitees,
        'dernieres_plaintes': dernieres_plaintes,
    })


@login_required
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
def plainte_detail(request, pk):
    plainte = get_object_or_404(Plainte, pk=pk)
    return render(request, 'plaintes/plainte_detail.html', {'plainte': plainte})


@login_required
def plainte_create(request):
    if request.method == 'POST':
        form = PlainteForm(request.POST)
        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.modifie_par = request.user
            plainte.save()
            return redirect('plainte_detail', pk=plainte.pk)
    else:
        form = PlainteForm()

    return render(request, 'plaintes/plainte_form.html', {'form': form, 'titre': 'Ajouter une plainte'})


@login_required
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
def plainte_delete(request, pk):
    plainte = get_object_or_404(Plainte, pk=pk)

    if request.method == 'POST':
        plainte.delete()
        return redirect('plainte_list')

    return render(request, 'plaintes/plainte_confirm_delete.html', {'plainte': plainte})
