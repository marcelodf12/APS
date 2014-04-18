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
    ('atributo','atributo')
)
CLASE_PERMISOS = (
    ('VER','VER'),
    ('ADD','ADD'),
    ('MOD','MOD'),
    ('DEL','DEL'),
)
class Permisos(models.Model):
    permiso = models.CharField(max_length=30, choices=CLASE_PERMISOS)
    tipoObjeto = models.CharField(max_length=15, choices=TIPOS_PERMISOS)
    usuario = models.ForeignKey(User, null='True', blank='True')
    grupo = models.ForeignKey(Group, null='True', blank='True')
    id_fk = models.IntegerField()

    def __unicode__(self):
        return self.permiso

    @staticmethod
    def valido(**kwargs):
        """
            Funcion que retorna True si se tienen los permisos necesarios
            :param usuario: Usuario
            :param permiso: Permiso
            :param tipoObjeto: Tipo de Objeto
            :param proyecto: Proyecto Opcional
            :param fase: fase Opcional
            :param item: Item Opcional
        """
        print kwargs.get('usuario')
        print kwargs.get('permiso')
        print kwargs.get('tipoObjeto')
        print kwargs.get('proyecto')
        print kwargs.get('fase')
        print kwargs.get('item')
        return False
