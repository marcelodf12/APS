from django.db import models
#from aps.aplicaciones.proyectos.models import Proyectos

# Create your models here.
class fases(models.Model):
    nombre = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    cantItems = models.IntegerField()
    estado = models.CharField(max_length=50)
#    proyecto = models.ForeignKey(Proyectos)

    def __unicode__(self):
        return self.nombre
