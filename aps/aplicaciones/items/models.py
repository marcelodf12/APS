from django.db import models

from aps.aplicaciones.fases.models import fases


# ESTADOS = (
#     ('activo','activo'),
#     ('inactivo','inactivo'),
# )
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

class relacion(models.Model):
    """
    Este es el Modelo que define la relacion entre dos items
    """
    itemHijo = models.ForeignKey(items, null='True', related_name='hijo')
    itemPadre = models.ForeignKey(items, null='True', related_name='padre')
    estado = models.BooleanField()

    def __unicode__(self):
        """
        Metodo llamado para visualizar relacion. Muestra el nombre del item hijo seguido del nombre del item padre
        """
        return self.itemHijo.nombre + '-->' + self.itemPadre.nombre

class atributo(models.Model):
    """
    Este modelo define los atributos de un items
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=512)
    version = models.IntegerField(default='0')
    item = models.ForeignKey(items, null='true')