from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from app2.models import Project
# Create your views here.

def members(request):
  return render(request,'app2/templates/index.html')

def projekt(request):
  context = {'projects' : Project.objects.all()}
  return render(request,'app2/templates/projekt.html', context=context)

def projektansicht(request, given_id):
  all = Project.objects.all()
  obj = get_object_or_404(Project, id=given_id)
  context = {'project': obj, 'projects': all}
  return render(request,'app2/templates/projektansicht.html', context=context)  

def projekterstellen(request):
  if request.method == "GET":
    return render(request,'app2/templates/projekt-erstellen.html')
  
  if request.method == "POST":
    id = request.POST.get('id')
    titel = request.POST.get('titel')
    beschreibung = request.POST.get('beschreibung')
    ansprechpartner = request.POST.get('ansprechpartner')

    new_project = Project(id=id,titel=titel, beschreibung=beschreibung, ansprechpartner=ansprechpartner)
    new_project.save()

    return redirect('projektansicht')