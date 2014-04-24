from django.test import TestCase
from django.utils import unittest
from django.contrib.auth.models import User
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items
from django.test.client import Client

# Create your tests here.

class TestEliminarItem(unittest.TestCase):
    """
        Prueba para comprobar si la eliminacion de usuarios se realiza de forma logica
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            self.userLogin = User.objects.create_user(username="fulano Login", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider"
            userRegistrado.password = "123"
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
            proyectoRegistrado.nombre = "proyecto Registrado"
            proyectoRegistrado.cantFases = 7
            proyectoRegistrado.fechaInicio = "2014-03-03"
            proyectoRegistrado.lider = userRegistrado
            proyectoRegistrado.save()

            #Creacion de una fase para instanciar un item
            faseRegistrada = fases()
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.save()

            #Creacion de un item para la eliminacion
            itemRegistrado = items()
            itemRegistrado.pk = 1
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para modificar el item con id=1
        response = self.cliente.post("/items/eliminar/1",data={'comentario':'eliminacion item de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        #Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
        e = items.objects.get(nombre="item Registrado", complejidad=10, versionAct=1, estado="eliminado" )


        # print "\nNombre del item: ", e.nombre                     # Nombre del item borrado
        # print "Complejidad del item: ", e.complejidad             # Complejidad del item borrado
        # print "Version actual:", e.versionAct                     # Version actual del item borrado
        # print "Estado del item:", e.estado                        # Estado del item borrado

class TestCrearItem(unittest.TestCase):


    def setUp(self):
        # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(username="fulano Login2", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider2"
            userRegistrado.password = "123"
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
            proyectoRegistrado.nombre = "proyecto Registrado"
            proyectoRegistrado.cantFases = 7
            proyectoRegistrado.fechaInicio = "2014-03-03"
            proyectoRegistrado.lider = userRegistrado
            proyectoRegistrado.save()

            #Creacion de una fase para instanciar un item
            faseRegistrada = fases()
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.save()


    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login2', password='123')

        # Peticion POST para modificar el item con id=1
        response = self.cliente.post("/items/crear/1",data={'nombre':'item prueba',
                                                           'versionAct':'1',         #Esto debe ser automatico
                                                           'estado':'creado',        #Esto debe ser automatico
                                                           'complejidad':'5',
                                                           'fase':'1'
                                                           })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        # Se consulta si el usuario fue borrado, si su estado fue cambiado a 'False'
        e = items.objects.get(nombre="item prueba",
                              versionAct="1",       #Esto debe ser automatico
                              estado="creado",      #Esto debe ser automatico
                              complejidad="5",
                              fase="1")

        #print "\nNombre del item: ", e.nombre                     # Nombre del item creado
        #print "Complejidad del item: ", e.complejidad             # Complejidad del item creado
        #print "Version actual:", e.versionAct                     # Version actual del item creado
        #print "Estado del item:", e.estado                        # Estado del item creado

        #self.assertEqual(e.estado, "creado")
        #self.assertFalse(e.is_active)


if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()
