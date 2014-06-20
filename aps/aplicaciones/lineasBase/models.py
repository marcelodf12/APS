"""
    Modelos definidos para la aplicacion lineasBase
"""

from django.db import models

# Create your models here.

from aps.aplicaciones.items.models import items
from aps.aplicaciones.fases.models import fases

class lineasBase(models.Model):
    """Este es el modelo 'lineasBase' con sus atributos, al sincronizar con la Base de Datos la clase se convertira
     en una tabla y sus atributos se traduciran en campos de la misma. """

    nombre = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    fase = models.ForeignKey(fases)

    def __unicode__(self):
        """
            Metodo que es invocado para mostrar el objeto como una cadena.En este caso se mostrara el valor del
            atributo nombre para cada instancia del modelo lineasBase
        """
        return self.nombre

class relacionItemLineaBase(models.Model):
    item = models.OneToOneField(items)
    linea = models.ForeignKey(lineasBase)
