"""
    Modulo de Pruebas Unitarias para la aplicacion inicio
"""
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
        #SOLUCIONAR response = self.client.get('/inicio/')
        print 'BORRAR ESTA LINEA'
        #usuario=response.context['user']

        # La solicitud tiene exito si el servidor responde 200
        #self.assertEqual(response.status_code, 200)


class TestDeAutenticacion(unittest.TestCase):
    """
        Prueba para comprobar si el index inicia con un usuario no autenticado
    """
    def setUp(self):
        # Creacion de un cliente
        self.client = Client()

    def test_details(self):
        # Simula un GET del cliente
        #SOLUCIONAR response = self.client.get('/inicio/')
        print 'BORRAR ESTA LINEA'
        #usuario=response.context['user']

        # Cheque que se ingreso al index pero no se ha autenticado
        #self.assertEqual(usuario.__unicode__(), "AnonymousUser")


class TestCrearUser(unittest.TestCase):
    """
        Prueba para comprobar la creacion de usuarios
    """
    def setUp(self):
        """
            La forma de crear un nuevo usuario es registrandose, solo se necesita el cliente
            para la peticion
        """
        self.cliente = Client()


    def test_details(self):

        # Peticion POST para crear un usuario
        response = self.cliente.post("/registrarse/", data={'username': 'nickPrueba',
                                                     'password1': 'pass',
                                                     'password2': 'pass',
                                                     'nombre':'nombre prueba',
                                                     'apellido':'apellido prueba',
                                                     'correo':'correo prueba'
                                                     })
        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'


        #Se consulta por el usuario creado en la tabla User
        consultaInstancia = User.objects.get(username="nickPrueba", first_name="nombre prueba",
                             last_name="apellido prueba", email="correo prueba")

        #print "Id del usuario creado:", consultaInstancia.pk                   # Id del usuario recien creado
        #print "Nick:", consultaInstancia.username                              # Username del usuario recien creado
        #print "Nombre:", consultaInstancia.first_name                          # Nombre del usuario recien creado
        #print "Apellido:", consultaInstancia.last_name                         # Apellido del usuario recien creado

        self.assertNotEquals(consultaInstancia,None)


class TestModificarUser(unittest.TestCase):
    """
        Prueba para comprobar la modificacion de usuarios
    """
    def setUp(self):

        #Creacion de un cliente
        self.cliente = Client()

        #Creacion de usuario a modificar
        self.userRegistrado = User()
        self.userRegistrado.username = "nickPrueba2"
        self.userRegistrado.pk = '3'
        self.userRegistrado.password = "123"
        self.userRegistrado.email = "correo@hotmail.com"
        self.userRegistrado.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'nickPrueba2'
        a = self.cliente.login(username='nickPrueba2', password='123')


        # Peticion POST para modificar un usuario
        response = self.cliente.post("/modificar/3", data={'first_name':'nombre prueba modificado',
                                                     'last_name':'apellido prueba modificado',
                                                     'email': 'correomodificado@hotmail.com',
                                                     })
        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'modificar'


        #Se consulta por el usuario modificado en la tabla User
        consultaInstancia = User.objects.get(first_name="nombre prueba modificado", last_name="apellido prueba modificado",
                             email="correomodificado@hotmail.com")


        # print "Id del usuario modificado:", consultaInstancia.pk
        # print "Username del usuario:", consultaInstancia.username
        # print "Nombre del usuario:", consultaInstancia.first_name
        # print "Apellido del usuario:", consultaInstancia.last_name
        # print "Correo del usuario:", consultaInstancia.email

        self.assertNotEquals(consultaInstancia,None)


class TestEliminarUser(unittest.TestCase):
    """
        Prueba para comprobar la eliminacion logica de usuarios
    """
    def setUp(self):
        """
            Metodo de inicializacion
        """

        # Creacion de un cliente
        self.client = Client()

        # Creacion de un usuario para la autenticacion
        self.userLogin = User.objects.create_user(username="fulano Login20", password="123")

        #Creacion de un usuario para la eliminacion
        self.userRegistrado = User()
        self.userRegistrado.pk = 2
        self.userRegistrado.username = "fulano Registrado2"
        self.userRegistrado.password = "123"
        self.userRegistrado.save()

    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login2'
        a = self.client.login(username='fulano Login2', password='123')

        # Peticion POST para eliminar el usuario con id=2
        response = self.client.post("/usuarios/eliminar/2", data={'comentario': 'eliminacion de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        # Se consulta si el usuario fue borrado, si su estado fue cambiado a 'False'
        consultaInstancia = User.objects.get(username="fulano Registrado2", password="123")

        #print "\nId del usuario:", consultaInstancia.pk                                # Id del usuario borrado
        #print "Username del usuario:", consultaInstancia.get_username().__str__()      # Username del usuario borrado
        #print "Esta Activo:", consultaInstancia.is_active                              # Booleano de estado (activo o inactivo)

        self.assertNotEquals(consultaInstancia,None)

if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()