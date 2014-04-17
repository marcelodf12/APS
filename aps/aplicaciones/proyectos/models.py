from django.db import models

# Create your models here.
class Proyectos(models.Model):
    """Este es el modelo 'Proyectos' con sus atributos, al sincronizar con la Base de Datos la clase se convertira
     en una tabla y sus atributos se traduciran en campos de la misma. """

    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    cantFases = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __unicode__(self):
        """ Metodo llamado para visualizar objetos. En este caso se mostrara el valor del atributo
        'nombre' para cada instancia del modelo Proyectos  """
        return self.nombre