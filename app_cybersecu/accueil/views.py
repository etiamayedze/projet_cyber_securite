from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return render(request, 'accueil/accueil.html', locals())
