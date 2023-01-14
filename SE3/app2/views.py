from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def members(request):
  return render(request,'app2/templates/index.html')

def projekt(request):
  return render(request,'app2/templates/projekt.html')