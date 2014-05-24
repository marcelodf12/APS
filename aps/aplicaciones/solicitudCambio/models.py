"""
    Modelos definidos para la aplicacion solictud de cambio
"""

from django.db import models

from aps.aplicaciones.lineasBase.models import lineasBase
from aps.aplicaciones.items.models import items
from django.contrib.auth.admin import User


# Create your models here.
class solicitudCambio(models.Model):

    descripcion = models.CharField(max_length=200)
    fechaExpiracion = models.DateField(null='True')
    lineaBase = models.ForeignKey(lineasBase, null='True')
    item = models.ForeignKey (items , null= 'true')
    costoAdicional = models.IntegerField(null='True')
    estado = models.CharField(max_length=50, default='pendiente')
    orden = models.IntegerField(null='True')
    usuario = models.ForeignKey(User, null='True')

    def __unicode__(self):
        return self.descripcion

class votos(models.Model):
    solicitud = models.ForeignKey(solicitudCambio)
    estado = models.CharField(max_length=50, default='pendiente')
    usuario = models.ForeignKey(User)
    aceptar = models.BooleanField(default=False)

