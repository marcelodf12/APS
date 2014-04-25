from django.test import TestCase
from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from aps.aplicaciones.fases.models import fases, Proyectos


# Create your tests here.
class TestCrearFase(unittest.TestCase):
    """ Prueba para comprobar la creacion de fases """

    def setUp(self):
        # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            userLogin = User.objects.create_user(username="fulano Login", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider"
            userRegistrado.password = "123"
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
            proyectoRegistrado.nombre = "proyecto Registrado"
            proyectoRegistrado.pk=1
            proyectoRegistrado.cantFases = 7
            proyectoRegistrado.fechaInicio = "2014-03-03"
            proyectoRegistrado.lider = userRegistrado
            proyectoRegistrado.save()



    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear un item con id=1
        response = self.cliente.post("/fases/crear/1",data={'nombre':'fase prueba',
                                                           'fechaInicio':'2014-04-03',
                                                           'cantItems':4,
                                                           'estado':'creado',
                                                           'proyecto':'1'
                                                           })

        print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        # Se consulta por el item creado en la tabla de items
        consultaInstancia = fases.objects.get(nombre="fase prueba",
                            fechaInicio="2014-04-03",
                            cantItems=4,
                            estado="creado",
                            proyecto="1")

        #print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre de la fase creada
        #print "Complejidad del item: ", consultaInstancia.fechaInicio             # Fecha de inicio de la fase creada
        #print "Version actual: ", consultaInstancia.cantItems                     # Cant. de items de la fase creada
        #print "Estado del item: ", consultaInstancia.estado                       # Estado de la fase creada
        #print "Proyecto asociado: ", consultaInstancia.proyecto                   # Proyecto de la fase creada

        self.assertNotEquals(consultaInstancia,None)


# class TestModificarItem(unittest.TestCase):
#     """Prueba para comprobar la modificacion de items"""
#
#     def setUp(self):
#         # Creacion de un cliente
#             self.cliente = Client()
#
#             # Creacion de un usuario para la autenticacion
#             userLogin = User.objects.create_user(username="fulano Login2", password="123")
#
#             #Creacion de un usuario Lider para instanciar un proyecto
#             userRegistrado = User()
#             userRegistrado.username = "fulano Lider2"
#             userRegistrado.password = "123"
#             userRegistrado.save()
#
#             #Creacion de un proyecto para instanciar una fase
#             proyectoRegistrado = Proyectos()
#             proyectoRegistrado.nombre = "proyecto Registrado"
#             proyectoRegistrado.cantFases = 7
#             proyectoRegistrado.fechaInicio = "2014-03-03"
#             proyectoRegistrado.lider = userRegistrado
#             proyectoRegistrado.save()
#
#             #Creacion de una fase para instanciar un item
#             faseRegistrada = fases()
#             faseRegistrada.nombre = "fase Registrada"
#             faseRegistrada.proyecto = proyectoRegistrado
#             faseRegistrada.versionAct = 1
#             faseRegistrada.complejidad = 10
#             faseRegistrada.cantItems = 6
#             faseRegistrada.fechaInicio = "2014-03-24"
#             faseRegistrada.save()
#
#             #Creacion de un item para la eliminacion
#             itemRegistrado = items()
#             itemRegistrado.pk = 1
#             itemRegistrado.nombre = "item Registrado"
#             itemRegistrado.fase = faseRegistrada
#             itemRegistrado.versionAct = 1
#             itemRegistrado.complejidad = 10
#             itemRegistrado.save()
#
#
#     def test_details(self):
#         # Cliente es autenticado como el usuario 'fulano Login'
#         b = self.cliente.login(username='fulano Login2', password='123')
#
#         # Peticion POST para modificar el item con id=1
#         response = self.cliente.post("/items/modificar/1",data={'nombre':'item prueba modificado',
#                                                            'versionAct':'2',         #Esto debe ser automatico
#                                                            'estado':'creado',        #Esto debe ser automatico
#                                                            'complejidad':'10',
#                                                            'fase':'1'
#                                                            })
#
#         #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'modificar'
#
#         # Se consulta por el item modificado en la tabla items
#         consultaInstancia = items.objects.get(nombre="item prueba modificado",
#                               versionAct="2",       #Esto debe ser automatico
#                               estado="creado",      #Esto debe ser automatico
#                               complejidad="10",
#                               fase="1")
#
#         #print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item modificado
#         #print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item modificado
#         #print "Version actual:", consultaInstancia.versionAct                     # Version actual del item modificado
#         #print "Estado del item:", consultaInstancia.estado                        # Estado del item modificado
#
#         self.assertNotEquals(consultaInstancia, None)
#
#
# class TestEliminarItem(unittest.TestCase):
#     """
#         Prueba para comprobar si la eliminacion de usuarios se realiza de forma logica
#     """
#     def setUp(self):
#
#             # Creacion de un cliente
#             self.cliente = Client()
#
#             # Creacion de un usuario para la autenticacion
#             self.userLogin = User.objects.create_user(username="fulano Login3", password="123")
#
#             #Creacion de un usuario Lider para instanciar un proyecto
#             userRegistrado = User()
#             userRegistrado.username = "fulano Lider3"
#             userRegistrado.password = "123"
#             userRegistrado.save()
#
#             #Creacion de un proyecto para instanciar una fase
#             proyectoRegistrado = Proyectos()
#             proyectoRegistrado.nombre = "proyecto Registrado"
#             proyectoRegistrado.cantFases = 7
#             proyectoRegistrado.fechaInicio = "2014-03-03"
#             proyectoRegistrado.lider = userRegistrado
#             proyectoRegistrado.save()
#
#             #Creacion de una fase para instanciar un item
#             faseRegistrada = fases()
#             faseRegistrada.nombre = "fase Registrada"
#             faseRegistrada.proyecto = proyectoRegistrado
#             faseRegistrada.versionAct = 1
#             faseRegistrada.complejidad = 10
#             faseRegistrada.cantItems = 6
#             faseRegistrada.fechaInicio = "2014-03-24"
#             faseRegistrada.save()
#
#             #Creacion de un item para la eliminacion
#             itemRegistrado = items()
#             itemRegistrado.pk = 1
#             itemRegistrado.nombre = "item Registrado"
#             itemRegistrado.fase = faseRegistrada
#             itemRegistrado.versionAct = 1
#             itemRegistrado.complejidad = 10
#             itemRegistrado.save()
#
#
#     def test_details(self):
#
#         # Cliente es autenticado como el usuario 'fulano Login'
#         b = self.cliente.login(username='fulano Login3', password='123')
#
#         # Peticion POST para eliminar el item con id=1
#         response = self.cliente.post("/items/eliminar/1",data={'comentario':'eliminacion item de prueba'})
#
#         #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'
#
#         #Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
#         consultaInstancia = items.objects.get(nombre="item Registrado", complejidad=10, versionAct=1, estado="eliminado" )
#
#
#         # print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item borrado
#         # print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item borrado
#         # print "Version actual:", consultaInstancia.versionAct                     # Version actual del item borrado
#         # print "Estado del item:", consultaInstancia.estado                        # Estado del item borrado


if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()