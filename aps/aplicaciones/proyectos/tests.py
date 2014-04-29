"""
    Modulo de Test para el Modelo  Proyecto
"""
from django.utils import unittest
from django.contrib.auth.models import User
from django.test.client import Client
from aps.aplicaciones.permisos.models import Permisos
from aps.aplicaciones.proyectos.models import Proyectos
from datetime import datetime

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

        # Se consulta por el item creado en la tabla de items
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


if __name__ == '__main__':
    unittest.main()