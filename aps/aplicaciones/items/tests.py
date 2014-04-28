from django.test import TestCase
from django.utils import unittest
from django.contrib.auth.models import User
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items
from django.test.client import Client

# Create your tests here.
class TestCrearItem(unittest.TestCase):
    """ Prueba para comprobar la creacion de items """

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
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-05"
            faseRegistrada.fechaInicioR = "2014-03-06"
            faseRegistrada.presupuesto=100000000
            faseRegistrada.save()


    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear un item con id=1
        # FALTA DEFINIR LO DEL ID DE LA FASE (URL)
        response = self.cliente.post("/items/crear/1",data={'nombre':'item prueba',
                                                            'complejidad':'5',
                                                            'costo':'2000'
                                                            })

        print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        # Se consulta por el item creado en la tabla de items
        consultaInstancia = items.objects.get(nombre="item prueba",
                              complejidad="5",
                              costo="2000")

        #print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item creado
        #print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item creado
        #print "Version actual: ", consultaInstancia.versionAct                    # Version actual del item creado
        #print "Estado: ", consultaInstancia.estado                                # Estado del item creado
        #print "Costo: ", consultaInstancia.costo                                  # Costo del item creado

        self.assertNotEquals(consultaInstancia,None)


class TestModificarItem(unittest.TestCase):
    """Prueba para comprobar la modificacion de items"""

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
            proyectoRegistrado.fechaFinP = "2014-10-03"
            proyectoRegistrado.fechaFinR = "2014-10-04"
            proyectoRegistrado.presupuesto=1500
            proyectoRegistrado.penalizacion=350
            proyectoRegistrado.save()

            #Creacion de una fase para instanciar un item
            faseRegistrada = fases()
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000

            faseRegistrada.save()

            #Creacion de un item para la modificacion
            itemRegistrado = items()
            itemRegistrado.pk = 1
            itemRegistrado.nombre = "item Registrado"
            #itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()


    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login2', password='123')

        # Peticion POST para modificar el item con id=1
        response = self.cliente.post("/items/modificar/1",data={'nombre':'item prueba modificado',
                                                        'complejidad':'11',
                                                        'costo':'2100'
                                                           })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'modificar'

        # Se consulta por el item modificado en la tabla items
        consultaInstancia = items.objects.get(nombre="item prueba modificado",
                              complejidad="11",
                              costo="2100")

        #print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item modificado
        #print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item modificado
        #print "Version actual: ", consultaInstancia.versionAct                    # Version actual del item modificado
        #print "Estado: ", consultaInstancia.estado                                # Estado del item modificado
        #print "Costo: ", consultaInstancia.costo                                  # Costo del item modificado

        self.assertNotEquals(consultaInstancia, None)


class TestEliminarItem(unittest.TestCase):
    """
        Prueba para comprobar si la eliminacion de usuarios se realiza de forma logica
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            self.userLogin = User.objects.create_user(username="fulano Login3", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider3"
            userRegistrado.password = "123"
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
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
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000
            faseRegistrada.save()

            #Creacion de un item para la eliminacion
            itemRegistrado = items()
            itemRegistrado.pk = 1
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login3', password='123')

        # Peticion POST para eliminar el item con id=1
        response = self.cliente.post("/items/eliminar/1",data={'comentario':'eliminacion item de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        #Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
        consultaInstancia = items.objects.get(nombre="item Registrado", complejidad=10, versionAct=1, estado="eliminado" )


        # print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item borrado
        # print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item borrado
        # print "Version actual:", consultaInstancia.versionAct                     # Version actual del item borrado
        # print "Estado del item:", consultaInstancia.estado                        # Estado del item borrado

        self.assertNotEquals(consultaInstancia, None)


if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()
