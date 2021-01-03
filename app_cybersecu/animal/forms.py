from django import forms
from .models import Parent, Animal, TypeAnimal, Medecin, Rendezvous


class Parent_form(forms.ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"


class Animal_form(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"


class TypeAnimal_form(forms.ModelForm):
    class Meta:
        model = TypeAnimal
        fields = "__all__"


class Medecin_form(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = "__all__"


class Rendezvous_form(forms.ModelForm):
    class Meta:
        model = Rendezvous
        fields = "__all__"
