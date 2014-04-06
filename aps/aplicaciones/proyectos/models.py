from django.db import models

# Create your models here.
class Proyectos(models.Model):
    nombre = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    cantFases = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre