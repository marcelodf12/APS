"""
    Modulo de pruebas para la aplicacion inicio
"""
from django.utils import unittest
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

if __name__ == '__main__':
    unittest.main()

