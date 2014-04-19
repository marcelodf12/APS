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
    ('INI','INI'),
    ('REV','REV')
)
class Permisos(models.Model):
    permiso = models.CharField(max_length=30, choices=CLASE_PERMISOS)
    tipoObjeto = models.CharField(max_length=15, choices=TIPOS_PERMISOS)
    usuario = models.ForeignKey(User, null='True', blank='True')
    grupo = models.ForeignKey(Group, null='True', blank='True')
    id_fk = models.IntegerField()

    def __unicode__(self):
        return self.permiso + ' ' + self.tipoObjeto + ' ' + str(self.id_fk) + ' ' + str(self.usuario)

    @staticmethod
    def valido(**kwargs):
        """
            Funcion que retorna True si se tienen los permisos necesarios
            :param usuario: Usuario
            :param grupo: Grupo
            :param permiso: Permiso
            :param tipoObjeto: Tipo de Objeto
            :param id: Clave foranea al objeto
        """
        u=kwargs.get('usuario')
        g=kwargs.get('grupo')
        p=kwargs.get('permiso')
        t=kwargs.get('tipoObjeto')
        i=kwargs.get('id')
        # print 'Permiso  : ' + p
        # print 'Usuario  : ' + str(u)
        # print 'Tipo     : ' + str(t)
        # print 'Id       : ' + str(i)
        grupos=Group.objects.filter(user__username=u)
        permU = Permisos.objects.filter(usuario__username=u).filter(tipoObjeto=t).filter(id_fk=i).filter(permiso=p)
        if permU:
            return True
        else:
            for g in grupos:
                permG = Permisos.objects.filter(grupo__name=g).filter(tipoObjeto=t).filter(id_fk=i).filter(permiso=p)
                if permG:
                    return True
        return False
