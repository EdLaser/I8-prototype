from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app2.models import tablet
# Create your views here.

def members(request):
  return render(request,'app2/templates/index.html')

def projekt(request):
  return render(request,'app2/templates/projekt.html')

def projektansicht(request):
  return render(request,'app2/templates/projektansicht.html')  


def projekterstellen(request):
  if request.method == "GET":
    return render(request,'app2/templates/projekt-erstellen.html')
  if request.method == "POST":
    ID = request.POST.get('id')
    Titel = request.POST.get('Titel')
    Beschreibung = request.POST.get('Beschreibung')
    Ansprechpartner = request.POST.get('Ansprechpartner')

    new_tablet = tablet(ID,Titel,Beschreibung,Ansprechpartner )
    new_tablet.save()

    return render(request,'app2/templates/projektansicht.html')