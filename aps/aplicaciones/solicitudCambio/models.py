"""
    Modelos definidos para la aplicacion fases
"""

from django.db import models

from aps.aplicaciones.lineasBase.models import lineasBase
from aps.aplicaciones.items.models import items


# Create your models here.
class solicitudCambio(models.Model):

    descripcion = models.CharField(max_length=200)
    fechaExpiracion = models.DateField()
    #lineaBase = models.foreinkey(lineasBase, null='True')
    item = models.foreonkey (items , null= 'true')
    costoAdicional = models.IntegerField(null='True')
    estado = models.CharField(max_length=50, default='pendiente')
    orden = models.IntegerField(null='True')

    def __unicode__(self):
        return self.descripcion

