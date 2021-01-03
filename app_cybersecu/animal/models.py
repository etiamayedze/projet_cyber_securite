from django.db import models


# Create your models here.

class Parent(models.Model):
    nom_parent = models.CharField(max_length=30)
    prenom_parent = models.CharField(max_length=45)
    tel_parent = models.CharField(max_length=15)
    email_parent = models.EmailField(max_length=30)
    adresse_parent = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_parent + ' ' + self.prenom_parent


class TypeAnimal(models.Model):
    libelle_type_animal = models.CharField(max_length=30)

    def __str__(self):
        return self.libelle_type_animal


class Animal(models.Model):
    nom_animal = models.CharField(max_length=30)
    sexe_animal = models.CharField(max_length=1)
    parent_animal = models.ForeignKey(Parent, on_delete=models.CASCADE)
    type_animal = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_animal


class Medecin(models.Model):
    nom_medecin = models.CharField(max_length=30)
    prenom_medecin = models.CharField(max_length=30)
    contact_medecin = models.CharField(max_length=15)

    def __str__(self):
        return self.nom_medecin + ' ' + self.prenom_medecin


class Rendezvous(models.Model):
    date_rendezvous = models.DateField(auto_now=False)
    heure_rendezvous = models.TimeField(default=None)
    medecin_rdv = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    animal_rdv = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal_rdv.nom_animal
