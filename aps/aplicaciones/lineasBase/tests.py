from django.utils import unittest
from django.test import TestCase
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items
from aps.aplicaciones.permisos.models import Permisos
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.lineasBase.models import lineasBase
from django.test.client import Client
from django.contrib.auth.models import User

# Create your tests here.
class TestCrearLineaBase(unittest.TestCase):
    """
        Prueba para comprobar la creacion de Lineas Base
    """
    def setUp(self):
            """
                Metodo de inicializacion
            """

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(pk=1, username="fulano Login", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider2"
            userRegistrado.password = "123"
            userRegistrado.pk = 2
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
            proyectoRegistrado.pk = 1
            proyectoRegistrado.nombre = "proyecto Registrado"
            proyectoRegistrado.cantFases = 7
            proyectoRegistrado.fechaInicio = "2014-03-03"
            proyectoRegistrado.lider = userRegistrado
            proyectoRegistrado.fechaFinP = "2014-10-03"
            proyectoRegistrado.fechaFinR = "2014-10-04"
            proyectoRegistrado.presupuesto=1500
            proyectoRegistrado.penalizacion=350
            proyectoRegistrado.save()

            #Creacion de una fase para instanciar un item
            faseRegistrada = fases()
            faseRegistrada.pk = 1
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de items para la modificacion
            itemRegistrado = items()
            itemRegistrado.pk = 1
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()

            itemRegistrado2 = items()
            itemRegistrado2.pk = 2
            itemRegistrado2.fase = faseRegistrada
            itemRegistrado2.nombre = "item Registrado"
            itemRegistrado2.versionAct = 1
            itemRegistrado2.complejidad = 10
            itemRegistrado2.costo = 2000
            itemRegistrado2.save()

            itemRegistrado3 = items()
            itemRegistrado3.pk = 3
            itemRegistrado3.fase = faseRegistrada
            itemRegistrado3.nombre = "item Registrado"
            itemRegistrado3.versionAct = 1
            itemRegistrado3.complejidad = 10
            itemRegistrado3.costo = 2000
            itemRegistrado3.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear una Linea Base
        response = self.cliente.post("/lineasBase/crear/1",data={'idFase':'1',
                                                                 'nombre':'nom1',
                                                                 'idItems':'1',
                                                                 'idItems':'2', # ESTO ES CORRECTO? --- LISTA DE ITEMS
                                                            })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        # Se consulta por el permiso creado en la tabla de lineas base
        consultaInstancia = lineasBase.objects.get(nombre="nom1",
                             #estado="creado",
                             fase=1
                             )

        #print "\nNombre de Linea Base: ", consultaInstancia.nombre
        #print "Estado: ", consultaInstancia.estado
        #print "Fase: ", consultaInstancia.fase

        self.assertNotEquals(consultaInstancia,None)