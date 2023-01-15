from django.db import models

# Create your models here.

class Project(models.Model):
  id = models.AutoField(primary_key=True, default=0)
  titel = models.CharField(max_length=255)
  beschreibung = models.CharField(max_length=255)
  ansprechpartner = models.CharField(max_length=255)
