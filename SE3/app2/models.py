from django.db import models

# Create your models here.

class Project(models.Model):
  id = models.CharField(max_length = 255,primary_key=True)
  titel = models.CharField(max_length=255)
  beschreibung = models.CharField(max_length=255)
  ansprechpartner = models.CharField(max_length=255)
