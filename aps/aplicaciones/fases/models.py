from django.db import models

# Create your models here.
class fases(models.Model):
    nombre = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    cantItems = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre