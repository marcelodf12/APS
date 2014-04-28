from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyectos(models.Model):
    """Este es el modelo 'Proyectos' con sus atributos, al sincronizar con la Base de Datos la clase se convertira
     en una tabla y sus atributos se traduciran en campos de la misma. """

    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFinP = models.DateField()
    fechaFinR = models.DateField(null='True')
    cantFases = models.IntegerField()
    estado = models.CharField(max_length=50, default='creado')
    presupuesto = models.IntegerField()
    penalizacion= models.IntegerField()
    saldo = models.IntegerField(null='True')
    lider = models.ForeignKey(User, null='True')

    def __unicode__(self):
        """ Metodo llamado para visualizar objetos. En este caso se mostrara el valor del atributo
        'nombre' para cada instancia del modelo Proyectos  """
        return self.nombre