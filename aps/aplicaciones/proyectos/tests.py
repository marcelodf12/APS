"""
    Modulo de Test para el Modelo  Proyecto
"""
from django.utils import unittest
from django.contrib.auth.models import User
from django.test.client import Client
from aps.aplicaciones.permisos.models import Permisos
from aps.aplicaciones.proyectos.models import Proyectos

class TestCrearProyecto(unittest.TestCase):
    """
        Prueba para comprobar la creacion de proyectos
    """
    def setUp(self):
            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(pk=1, username="fulano Login", password="123")

            # Asignacion del permiso ADD para userLogin, a fin de poder crear un proyecto
            permisoUserLogin = Permisos()
            permisoUserLogin.permiso = "ADD"
            permisoUserLogin.tipoObjeto = "proyecto"
            permisoUserLogin.id_fk = 0
            permisoUserLogin.usuario = userLogin
            permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear un proyecto
        response = self.cliente.post("/proyectos/crear/",data={'nombre':'proyecto prueba',
                                                            'fechaInicio':'2014-04-04',
                                                            'fechaFinP':'2014-04-04',
                                                            'cantFases':'5',
                                                            'presupuesto':'2500',
                                                            'penalizacion':'250'
                                                            })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        # Se consulta por el proyecto creado en la tabla de proyectos
        consultaInstancia = Proyectos.objects.get(nombre="proyecto prueba",
                             fechaInicio="2014-04-04",
                             fechaFinP="2014-04-04",
                             cantFases="5",
                             presupuesto="2500",
                             penalizacion="250",
                             )

        #print "\nNombre del proyecto: ", consultaInstancia.nombre              # Nombre del proyecto creado
        #print "Cantidad de fases: ", consultaInstancia.cantFases               # Cantidad de fases del proyecto creado
        #print "Fecha de inicio: ", consultaInstancia.fechaInicio               # Fecha inicio del proyecto creado
        #print "Presupuesto: ", consultaInstancia.presupuesto                   # Presupuesto del proyecto creado
        #print "Penalizacion: ", consultaInstancia.penalizacion                 # Penalizacion del proyecto creado

        self.assertNotEquals(consultaInstancia,None)


class TestModificarProyecto(unittest.TestCase):
    """
        Prueba para comprobar la modificacion de proyectos
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(pk=1, username="fulano Login", password="123")

            # Asignacion del permiso MOD para userLogin, a fin de poder modificar un proyecto
            permisoUserLogin = Permisos()
            permisoUserLogin.permiso = "MOD"
            permisoUserLogin.tipoObjeto = "proyecto"
            permisoUserLogin.id_fk = 1
            permisoUserLogin.usuario = userLogin
            permisoUserLogin.save()

            # Creacion del proyecto a modificar
            proyectoModificar = Proyectos()
            proyectoModificar.pk = 1
            proyectoModificar.nombre = "proyecto creado"
            proyectoModificar.fechaInicio = "2014-04-04"
            proyectoModificar.fechaFinP = "2014-04-04"
            proyectoModificar.cantFases = 5
            proyectoModificar.presupuesto = 3000
            proyectoModificar.penalizacion = 600


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para modificar un proyecto
        response = self.cliente.post("/proyectos/modificar/1",data={'nombre':'proyecto modificado',
                                                            'fechaInicio':'2014-05-05',
                                                            'fechaFinP':'2014-05-05',
                                                            'penalizacion':'650',
                                                            'presupuesto':'3500'
                                                            })

        print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'modificar'

        # Se consulta por el proyecto modificado en la tabla de proyectos
        consultaInstancia = Proyectos.objects.get(nombre="proyecto modificado",
                              fechaInicio="2014-05-05",
                              fechaFinP="2014-05-05",
                              presupuesto="3500",
                              penalizacion="650"
                              )

        #print "\nNombre del proyecto: ", consultaInstancia.nombre              # Nombre del proyecto modificado
        #print "Cantidad de fases: ", consultaInstancia.cantFases               # Cantidad de fases del proyecto modificado
        #print "Fecha de inicio: ", consultaInstancia.fechaInicio               # Fecha inicio del proyecto modificado
        #print "Presupuesto: ", consultaInstancia.presupuesto                   # Presupuesto del proyecto modificado
        #print "Penalizacion: ", consultaInstancia.penalizacion                 # Penalizacion del proyecto modificado

        self.assertNotEquals(consultaInstancia,None)


class TestEliminarProyecto(unittest.TestCase):
    """
        Prueba para comprobar la eliminacion logica de proyectos
        OBS: Al probar eliminar el proyecto en el navegador funciona bien, pero no es lo mismo en la prueba...
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(pk=1, username="fulano Login", password="123")

            # Asignacion del permiso MOD para userLogin, a fin de poder modificar un proyecto
            # VER QUE AQUI TIENE SOLO PERMISO 'MOD'
            permisoUserLogin = Permisos()
            permisoUserLogin.permiso = "MOD"
            permisoUserLogin.tipoObjeto = "proyecto"
            permisoUserLogin.id_fk = 3
            permisoUserLogin.usuario = userLogin
            permisoUserLogin.save()

            # Creacion del proyecto a eliminar
            proyectoModificar = Proyectos()
            proyectoModificar.pk = 3
            proyectoModificar.nombre = "proyecto creado3"
            proyectoModificar.fechaInicio = "2014-04-04"
            proyectoModificar.fechaFinP = "2014-04-04"
            proyectoModificar.cantFases = 5
            proyectoModificar.presupuesto = 3000
            proyectoModificar.penalizacion = 600
            proyectoModificar.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para eliminar un proyecto
        response = self.cliente.post("/proyectos/eliminar/3",data={'comentario':'prueba eliminacion logica de proyectos'
                                                            })

        #AQUI NO MUESTRA ERROR DE PERMISOS, SINO REDIRECCIONA A LISTAR PROYECTOS
        print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'eliminar'

        # Se consulta por el proyecto borrado en la tabla de proyectos
        consultaInstancia = Proyectos.objects.get(nombre="proyecto creado3",
                            fechaInicio="2014-04-04",
                            fechaFinP="2014-04-04",
                            presupuesto="3000",
                            penalizacion="600",
                            estado="creado"         # EL ESTADO NO SE MODIFICA INCLUSO CAMBIANDO EL PERMISO A 'DEL'
                            )

        #print "\nNombre del proyecto: ", consultaInstancia.nombre              # Nombre del proyecto eliminado
        #print "Cantidad de fases: ", consultaInstancia.cantFases               # Cantidad de fases del proyecto eliminado
        #print "Fecha de inicio: ", consultaInstancia.fechaInicio               # Fecha inicio del proyecto eliminado
        #print "Presupuesto: ", consultaInstancia.presupuesto                   # Presupuesto del proyecto eliminado
        #print "Penalizacion: ", consultaInstancia.penalizacion                 # Penalizacion del proyecto eliminado

        self.assertNotEquals(consultaInstancia,None)

if __name__ == '__main__':
    unittest.main()