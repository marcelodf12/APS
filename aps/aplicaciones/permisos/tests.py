"""
    Modulo de Test para el Modelo Permisos
"""
from django.utils import unittest
from django.contrib.auth.models import User
from django.test.client import Client
from aps.aplicaciones.permisos.models import Permisos
from aps.aplicaciones.proyectos.models import Proyectos

class TestCrearPermiso(unittest.TestCase):
    """
        Prueba para comprobar la creacion de permisos
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(pk=1, username="fulano Login", password="123")

            # Creacion del usuario al que se asignara el permiso
            userModificar = User.objects.create_user(pk=2, username="fulano add", password="123")

            # Asignacion del permiso ADD para userLogin, a fin de poder crear un permiso
            permisoUserLogin = Permisos()
            permisoUserLogin.permiso = "ADD"
            permisoUserLogin.tipoObjeto = "permiso"
            permisoUserLogin.id_fk = 0
            permisoUserLogin.usuario = userLogin
            permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear un permiso
        response = self.cliente.post("/permisos/crear/",data={'permiso':'ADD',
                                                            'tipoObjeto':'permiso',
                                                            'usuario':'2',
                                                            'grupo':'',
                                                            'id_fk':'2'
                                                            })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        # Se consulta por el permiso creado en la tabla de permiso
        #PROBLEMA CUANDO SE TIENE MUCHOS REGISTROS QUE CUMPLEN
        consultaInstancia = Permisos.objects.get(permiso="ADD",
                            tipoObjeto="permiso",
                            usuario="2",
                            id_fk="2"
                            )

        #print "\nTipo de permiso: ", consultaInstancia.permiso            # Tipo de permiso creado
        #print "Tipo Objeto: ", consultaInstancia.tipoObjeto               # Tipo de objeto sobre el cual se crea el permiso
        #print "Usuario: ", consultaInstancia.usuario                      # Usuario al cual es asignado el permiso
        #print "Grupo: ", consultaInstancia.grupo                          # Grupo al cual se aplica el permiso
        #print "Id del objeto: ", consultaInstancia.id_fk                  # Id del objeto sobre el cual se crea el permiso

        self.assertNotEquals(consultaInstancia,None)


class TestEliminarPermiso(unittest.TestCase):
    """
        Prueba para comprobar la eliminacion de permisos
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(pk=1, username="fulano Login", password="123")

            # Creacion del usuario cuyo permiso sera eliminado
            self.userEliminar = User.objects.create_user(pk=2, username="fulano Modify", password="123")

            # Asignacion del permiso DEL para userLogin, a fin de poder eliminar un permiso
            permisoUserLogin = Permisos()
            permisoUserLogin.pk = 2
            permisoUserLogin.permiso = "DEL"
            permisoUserLogin.tipoObjeto = "permiso"
            permisoUserLogin.id_fk = 3
            permisoUserLogin.usuario = userLogin
            permisoUserLogin.save()

            # Creacion del permiso que sera eliminado
            permisoEliminar = Permisos()
            permisoEliminar.pk = 3
            permisoEliminar.permiso = "ADD"
            permisoEliminar.tipoObjeto = "permiso"
            permisoEliminar.id_fk = 0
            permisoEliminar.usuario = self.userEliminar
            permisoEliminar.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para eliminar un permiso
        response = self.cliente.post("/permisos/eliminar/3")

        print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'eliminar'


        # Creamos un permiso con el mismo id del permiso anteriormente eliminado. La idea es demostrar que el permiso
        # fue fisicamente eliminado, creando otro permiso con el mismo id
        permisoRestaurado = Permisos()
        permisoRestaurado.pk = 3
        permisoRestaurado.permiso = "ADD"
        permisoRestaurado.tipoObjeto = "permiso"
        permisoRestaurado.id_fk = 0
        permisoRestaurado.usuario = self.userEliminar
        permisoRestaurado.save()

        # Compara el valor del id del permiso que volvimos a crear con el id del permiso que fue eliminado
        self.assertNotEqual(permisoRestaurado.pk,"3")


if __name__ == '__main__':
    unittest.main()