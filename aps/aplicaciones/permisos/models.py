from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items


# Create your models here.
TIPOS_PERMISOS = (
    ('proyecto','proyecto'),
    ('fase','fase'),
    ('item','item'),
    ('permiso','permiso'),
)
CLASE_PERMISOS = (
    ('VER','VER'),
    ('ADD','ADD'),
    ('MODIFICAR','MODIFICAR'),
    ('DELETE','DELETE'),
)
class Permisos(models.Model):
    permiso = models.CharField(max_length=30, choices=CLASE_PERMISOS)
    tipoObjeto = models.CharField(max_length=15, choices=TIPOS_PERMISOS)
    usuario = models.ForeignKey(User, null='True', blank='True')
    grupo = models.ForeignKey(Group, null='True', blank='True')
    proyecto = models.ForeignKey(Proyectos, null='True', blank='True')
    fases = models.ForeignKey(fases, null='True', blank='True')
    items = models.ForeignKey(items, null='True', blank='True')

    def __unicode__(self):
        return self.permiso