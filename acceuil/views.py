from django.shortcuts import render
from .models import Acceuilperso, Contenus, Visite

def contenu(request):
    query = request.GET.get('q', '')
    if query:
        contenus = Contenus.objects.filter(titre__icontains=query).order_by('-date_creation')
    else:
        contenus = Contenus.objects.all().order_by('-date_creation')
    return render(request, 'blogs.html', {'contenus': contenus})

def acceuil(request):
    # Enregistre une visite à chaque affichage
    Visite.objects.create()
    acceuils = Acceuilperso.objects.all()
    total_visites = Visite.objects.count()
    return render(request, 'acceuil.html', {'acceuils': acceuils, 'total_visites': total_visites})
