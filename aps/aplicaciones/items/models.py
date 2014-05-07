"""
    Modelos definidos para la aplicacion items
"""

from django.db import models

from aplicaciones.fases.models import fases


# Create your models here.
class items(models.Model):
    """Este es el modelo 'items' con sus atributos, al sincronizar con la Base de Datos la clase se convertira
    en una tabla y sus atributos se traduciran en campos de la misma. """

    nombre = models.CharField(max_length=100)
    versionAct = models.IntegerField(default='1')
    estado = models.CharField(max_length=15, default='creado')
    complejidad = models.IntegerField()
    fase = models.ForeignKey(fases, null='True')
    costo = models.IntegerField()

    def __unicode__(self):
        """ Metodo llamado para visualizar objetos. En este caso se mostrara el valor del atributo 'nombre' para
         cada instancia del modelo items """
        return self.nombre