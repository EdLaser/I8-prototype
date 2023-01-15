from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from app2.models import Project
# Create your views here.

def members(request):
  return render(request,'app2/templates/index.html')

def projekt(request):
  return render(request,'app2/templates/projekt.html')

def projektansicht(request, given_id):
  wanted_project = Project.objects.filter(id=given_id)
  return render(request,'app2/templates/projektansicht.html', project = wanted_project)  


def projekterstellen(request):
  if request.method == "GET":
    return render(request,'app2/templates/projekt-erstellen.html')
  if request.method == "POST":
    titel = request.POST.get('titel')
    beschreibung = request.POST.get('Bbeschreibung')
    ansprechpartner = request.POST.get('ansprechpartner')

    new_project = Project(titel,beschreibung,ansprechpartner )
    new_project.save()

    return redirect('projektansicht', given_id = new_project.id)