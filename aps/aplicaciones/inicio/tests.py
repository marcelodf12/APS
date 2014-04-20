"""
    Modulo de pruebas para la aplicacion inicio
"""
from django.test import TestCase
from django.utils import unittest
from django.contrib.auth.models import User
from django.test.client import Client

class TestDeRespuestaDeServidor(unittest.TestCase):
    """
        Prueba para comprobar si el servidor responde correctamente
    """
    def setUp(self):
        # Creacion de un cliente
        self.client = Client()

    def test_details(self):
        # Simula un GET del cliente
        response = self.client.get('/inicio/')
        usuario=response.context['user']

        # La solicitud tiene exito si el servidor responde 200
        self.assertEqual(response.status_code, 200)

class TestDeAutenticacion(unittest.TestCase):
    """
        Prueba para comprobar si el index inicia con un usuario no autenticado
    """
    def setUp(self):
        # Creacion de un cliente
        self.client = Client()

    def test_details(self):
        # Simula un GET del cliente
        response = self.client.get('/inicio/')
        usuario=response.context['user']

        # Cheque que se ingreso al index pero no se ha autenticado
        self.assertEqual(usuario.__unicode__(), "AnonymousUser")


class TestEliminarUser(unittest.TestCase):
    """
        Prueba para comprobar si la eliminacion de usuarios se realiza de forma logica
    """
    def setUp(self):

        # Creacion de un cliente
        self.client = Client()

        # Creacion de un usuario para la autenticacion
        self.userLogin = User.objects.create_user(username="fulano Login", password="123")

        #Creacion de usuarios para la eliminacion
        #self.userRegistrado = User.objects.create_user(username="fulano Registrado 1", password="123")
        self.userRegistrado = User()
        self.userRegistrado.username = "fulano Registrado 1"
        self.userRegistrado.password = "123"
        self.userRegistrado.save()

    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        a = self.client.login(username='fulano Login', password='123')

        # Peticion POST para eliminar el usuario con id=2
        response = self.client.post("/usuarios/eliminar/2", data={'comentario': 'eliminacion de prueba'})
        #print self.userRegistrado.is_active     #PORQUE ESTO DA TRUE!!!!!!!!!  BORRAR LINEA

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        # Se consulta si el usuario fue borrado, si su estado fue cambiado a 'False'
        e = User.objects.get(username="fulano Registrado 1", password="123", is_active=False)

        #print "\nId del usuario:", e.pk                                # Id del usuario borrado
        #print "Username del usuario:", e.get_username().__str__()      # Username del usuario borrado
        #print "Esta Activo:", e.is_active                              # Booleano de estado (activo o inactivo)

if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()