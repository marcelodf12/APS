from django.db import models
from django.contrib.auth.models import User
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items


# Create your models here.
class Permisos(models.Model):
    permiso = models.CharField(max_length=30)
    tipoObjeto = models.CharField(max_length=15)
    usuario = models.ForeignKey(User)
    proyecto = models.ForeignKey(Proyectos, null='true')
    fases = models.ForeignKey(fases, null='true')
    items = models.ForeignKey(items, null='true')

    def __unicode__(self):
        return self.permiso

    @staticmethod
    def nuevo(permiso, tipoObjeto, objeto, usuario):
        pass