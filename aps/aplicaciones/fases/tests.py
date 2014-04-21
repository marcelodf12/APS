from django.test import TestCase
from django.utils import unittest
from django.contrib.auth.models import User
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items
from django.test.client import Client


class TestModificarUser(unittest.TestCase):
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

        # Peticion POST para eliminar el usuario con id=2
        #response = self.client.post("/usuarios/eliminar/2", data={'comentario': 'eliminacion de prueba'})
        #print self.userRegistrado.is_active     #PORQUE ESTO DA TRUE!!!!!!!!!  BORRAR LINEA

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        # Se consulta si el usuario fue borrado, si su estado fue cambiado a 'False'
        #e = User.objects.get(username="fulano Registrado 1", password="123", is_active=False)

        #print "\nId del usuario:", e.pk                                # Id del usuario borrado
        #print "Username del usuario:", e.get_username().__str__()      # Username del usuario borrado
        #print "Esta Activo:", e.is_active                              # Booleano de estado (activo o inactivo)

if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()