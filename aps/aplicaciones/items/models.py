from django.db import models

# Create your models here.
class items(models.Model):
    nombre = models.CharField(max_length=100)
    versionAct = models.IntegerField()
    estado = models.CharField(max_length=15)
    complejidad = models.IntegerField()

    def __unicode__(self):
        return self.nombre