from django.shortcuts import render, HttpResponse, redirect, get_list_or_404, get_object_or_404
from django import forms
from django.contrib import messages
from .models import Parent, Animal, TypeAnimal, Medecin, Rendezvous
from .forms import Parent_form, Animal_form, TypeAnimal_form, Medecin_form, Rendezvous_form
from django.contrib.auth.decorators import login_required


# Create your views here.

# vue pour enregistrer un parent
@login_required()
def parent(request):
    update = False
    parents = Parent.objects.all()
    if request.method == 'POST':
        parent_occurence = Parent_form(request.POST or None)

        if parent_occurence.is_valid():
            parent_occurence.save()
            messages.add_message(request, messages.INFO, 'Nouveau parent enregistré avec succès')
        else:
            return HttpResponse(parent_occurence.errors.as_json())

    return render(request, 'animal/parent.html', locals())


# vue pour modifier un parent
@login_required()
def updateparent(request):
    inst_parent = get_object_or_404(Parent, id=id)
    parents = Parent.objects.all()
    if request.method == 'GET':
        update = True
        return render(request, 'animal/parent.html', locals())
    else:
        form = Parent_form(request.POST or None, instance=inst_parent)
        if form.is_valid():
            inst_parent = form.save(commit=False)
            inst_parent.save()
        return redirect(parent)


# vue pour supprimer un parent
@login_required()
def deleteparent(request, id):
    parent_supprime = get_object_or_404(Parent, id=id)
    parent_supprime.delete()
    return redirect(parent)


# vue pour afficher la liste des parents
@login_required()
def listparent(request):
    parents = Parent.objects.all()
    return render(request, 'animal/listparent.html', locals())


# vue pour enregistrer un type animal
@login_required()
def typeanimal(request):
    update = False
    typeanimaux = TypeAnimal.objects.all()
    if request.method == 'POST':
        typeanimal_occurence = TypeAnimal_form(request.POST or None)

        if typeanimal_occurence.is_valid():
            typeanimal_occurence.save()
            messages.add_message(request, messages.INFO, 'Nouveau type animal enregistré avec succès')
        else:
            return HttpResponse(typeanimal_occurence.errors.as_json())

    return render(request, 'animal/typeanimal.html', locals())


# vue pour modifier un type animal
@login_required()
def updatetypeanimal(request):
    inst_typeanimal = get_object_or_404(TypeAnimal, id=id)
    typesanimaux = TypeAnimal.objects.all()
    if request.method == 'GET':
        update = True
        return render(request, 'animal/typeanimal.html', locals())
    else:
        form = TypeAnimal_form(request.POST or None, instance=inst_typeanimal)
        if form.is_valid():
            inst_typeanimal = form.save(commit=False)
            inst_typeanimal.save()
        return redirect(typeanimal)


# vue pour supprimer un type animal
@login_required()
def deletetypeanimal(request, id):
    typeanimal_supprime = get_object_or_404(TypeAnimal, id=id)
    typeanimal_supprime.delete()
    return redirect(typeanimal)


# vue pour afficher la liste des types animaux
@login_required()
def listtypeanimal(request):
    typesanimaux = TypeAnimal.objects.all()
    return render(request, 'animal/listetypeanimal.html', locals())


# vue pour enregistrer un animal
@login_required()
def animal(request):
    update = False
    animaux = Animal.objects.all()
    parents = Parent.objects.all()
    typeanimaux = TypeAnimal.objects.all()
    if request.method == 'POST':
        animal_occurence = Animal_form(request.POST or None)

        if animal_occurence.is_valid():
            animal_occurence.save()
            messages.add_message(request, messages.INFO, 'Nouvel animal enregistré avec succès')
        else:
            return HttpResponse(animal_occurence.errors.as_json())

    return render(request, 'animal/animal.html', locals())


# vue pour modifier un animal
@login_required()
def updateanimal(request):
    inst_animal = get_object_or_404(Animal, id=id)
    animaux = Animal.objects.all()
    if request.method == 'GET':
        update = True
        return render(request, 'animal/animal.html', locals())
    else:
        form = Animal_form(request.POST or None, instance=inst_animal)
        if form.is_valid():
            inst_animal = form.save(commit=False)
            inst_animal.save()
        return redirect(animal)


# vue pour supprimer un animal
@login_required()
def deleteanimal(request, id):
    animal_supprime = get_object_or_404(Animal, id=id)
    animal_supprime.delete()
    return redirect(animal)


# vue pour afficher la liste des animaux
@login_required()
def listanimaux(request):
    animaux = Animal.objects.all()
    parents = Parent.objects.all()
    return render(request, 'animal/listanimal.html', locals())


# vue pour enregistrer un medecin
@login_required()
def medecin(request):
    update = False
    medecins = Medecin.objects.all()
    if request.method == 'POST':
        medecin_occurence = Medecin_form(request.POST or None)

        if medecin_occurence.is_valid():
            medecin_occurence.save()
            messages.add_message(request, messages.INFO, 'Nouveau medecin enregistré avec succès')
        else:
            return HttpResponse(medecin_occurence.errors.as_json())

    return render(request, 'animal/medecin.html', locals())


# vue pour modifier un medecin
@login_required()
def updatemedecin(request):
    inst_medecin = get_object_or_404(Medecin, id=id)
    medecins = Medecin.objects.all()
    if request.method == 'GET':
        update = True
        return render(request, 'animal/medecin.html', locals())
    else:
        form = Medecin_form(request.POST or None, instance=inst_medecin)
        if form.is_valid():
            inst_medecin = form.save(commit=False)
            inst_medecin.save()
        return redirect(medecin)


# vue pour supprimer un medecin
@login_required()
def deletemedecin(request, id):
    medecin_supprime = get_object_or_404(Medecin, id=id)
    medecin_supprime.delete()
    return redirect(medecin)


# vue pour afficher la liste des medecins
def listmedecin(request):
    medecins = Medecin.objects.all()
    return render(request, 'animal/listmedecin.html', locals())


# vue pour enregistrer un rendez-vous
@login_required()
def rendezvous(request):
    update = False
    rdvs = Rendezvous.objects.all()
    animaux = Animal.objects.all()
    medecins = Medecin.objects.all()
    if request.method == 'POST':
        rendezvous_occurence = Rendezvous_form(request.POST or None)

        if rendezvous_occurence.is_valid():
            rendezvous_occurence.save()
            messages.add_message(request, messages.INFO, 'Nouveau rendez-vous enregistré avec succès')
        else:
            return HttpResponse(rendezvous_occurence.errors.as_json())

    return render(request, 'animal/rendezvous.html', locals())


# vue pour modifier un rendez-vous
@login_required()
def updaterendezvous(request):
    inst_rendezvous = get_object_or_404(Rendezvous, id=id)
    rdvs = Rendezvous.objects.all()
    if request.method == 'GET':
        update = True
        return render(request, 'animal/rendezvous.html', locals())
    else:
        form = Rendezvous_form(request.POST or None, instance=inst_rendezvous)
        if form.is_valid():
            inst_rendezvous = form.save(commit=False)
            inst_rendezvous.save()
        return redirect(rendezvous)


# vue pour supprimer un rendez-vous
@login_required()
def deleterendezvous(request, id):
    rendezvous_supprime = get_object_or_404(Rendezvous, id=id)
    rendezvous_supprime.delete()
    return redirect(rendezvous)


# vue pour afficher la liste des rendez-vous
@login_required()
def listrendezvous(request):
    rdvs = Rendezvous.objects.all()
    animaux = Animal.objects.all()
    parents = Parent.objects.all()
    return render(request, 'animal/listrendezvous.html', locals())
