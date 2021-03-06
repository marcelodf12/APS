"""
    Modelos definidos para la aplicacion fases
"""

from django.db import models

from aps.aplicaciones.proyectos.models import Proyectos


# Create your models here.
class fases(models.Model):

    nombre = models.CharField(max_length=100)
    fechaInicioP = models.DateField()
    fechaInicioR = models.DateField(null='True')
    estado = models.CharField(max_length=50, default='creado')
    proyecto = models.ForeignKey(Proyectos, null='True')
    costo = models.IntegerField(null='True')
    presupuesto = models.IntegerField()
    orden = models.IntegerField(null='True')

    def __unicode__(self):
        return self.nombre
