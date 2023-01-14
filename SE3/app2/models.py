from django.db import models

# Create your models here.

class tablet(models.Model):
  idd = models.CharField(max_length=255)
  Titel = models.CharField(max_length=255)
  beschreibnung = models.CharField(max_length=255)
  Ansprechpartner = models.CharField(max_length=255)
