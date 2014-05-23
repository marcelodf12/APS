from django.db import models

# Create your models here.

from aps.aplicaciones.items.models import items
from aps.aplicaciones.fases.models import fases

class lineasBase(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    fase = models.ForeignKey(fases)

class relacionItemLineaBase(models.Model):
    item = models.OneToOneField(items)
    linea = models.ForeignKey(lineasBase)
