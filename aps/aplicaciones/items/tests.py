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
        self.client = Client()

        # Creacion de un usuario para la autenticacion
        self.userLogin = User.objects.create_user(username="fulano Login", password="123")

        #Creacion de un usuario Lider para instanciar un proyecto
        self.userRegistrado = User()
        self.userRegistrado.username = "fulano Lider"
        self.userRegistrado.password = "123"
        self.userRegistrado.save()

        #Creacion de un proyecto para instanciar una fase
        self.proyectoRegistrado = Proyectos()
        self.proyectoRegistrado.nombre = "proyecto Registrado"
        self.proyectoRegistrado.cantFases = 7
        self.proyectoRegistrado.fechaInicio = "2014-03-03"
        self.proyectoRegistrado.lider = self.userRegistrado
        self.proyectoRegistrado.save()

        #Creacion de una fase para instanciar un item
        self.faseRegistrada = fases()
        self.faseRegistrada.nombre = "fase Registrada"
        self.faseRegistrada.proyecto = self.proyectoRegistrado
        self.faseRegistrada.versionAct = 1
        self.faseRegistrada.complejidad = 10
        self.faseRegistrada.cantItems = 6
        self.faseRegistrada.fechaInicio = "2014-03-24"
        self.faseRegistrada.save()

        #Creacion de un item para la eliminacion
        self.itemRegistrado = items()
        self.itemRegistrado.nombre = "item Registrado"
        self.itemRegistrado.fase = self.faseRegistrada
        self.itemRegistrado.versionAct = 1
        self.itemRegistrado.complejidad = 10
        self.itemRegistrado.save()

    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        a = self.client.login(username='fulano Login', password='123')

        # Peticion POST para modificar el item con id=1
        response = self.client.post("/items/eliminar/1",data={'comentario':'eliminacion item de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        # Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
        e = items.objects.get(nombre="item Registrado", complejidad=10, versionAct=1, estado="eliminado" )

        # print "\nNombre del item: ", e.nombre                     # Nombre del item borrado
        # print "Complejidad del item: ", e.complejidad             # Complejidad del item borrado
        # print "Version actual:", e.versionAct                     # Version actual del item borrado
        # print "Estado del item:", e.estado                        # Estado del item borrado

if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()