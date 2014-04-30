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
            proyectoRegistrado.fechaFinP = "2014-10-03"
            proyectoRegistrado.fechaFinR = "2014-10-04"
            proyectoRegistrado.presupuesto=1500
            proyectoRegistrado.penalizacion=350
            proyectoRegistrado.save()

            # Asignacion del permiso ADD para userRegistrado, a fin de poder crear una fase
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "ADD"
            # permisoUserLogin.tipoObjeto = "fases"
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()



    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear una fase
        # FALTA DEFINIR LO DEL ID DEL PROYECTO EN LA URL
        response = self.cliente.post("/fases/crearEnProyecto/",data={'nombre':'fase prueba',
                                                           'fechaInicioP':'2014-04-03',
                                                           'fechaInicioR':'2014-04-03',
                                                           'estado':'creado',
                                                           'presupuesto':'2000'
                                                           })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        # Se consulta por la fase creada en la tabla de items
        consultaInstancia = fases.objects.get(nombre="fase prueba",
                           fechaInicioP="2014-04-03",
                           estado="creado",
                           presupuesto="2000")

        #print "\nNombre de la fase: ", consultaInstancia.nombre                    # Nombre de la fase creada
        #print "Estado: ", consultaInstancia.estado                                 # Estado de la fase creada
        #print "Presupuesto: ", consultaInstancia.presupuesto                       # Presupuesto de la fase creada

        self.assertNotEquals(consultaInstancia,None)


class TestModificarFase(unittest.TestCase):
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
            proyectoRegistrado.pk=2
            proyectoRegistrado.cantFases = 7
            proyectoRegistrado.fechaInicio = "2014-03-03"
            proyectoRegistrado.lider = userRegistrado
            proyectoRegistrado.fechaFinP = "2014-10-03"
            proyectoRegistrado.fechaFinR = "2014-10-04"
            proyectoRegistrado.presupuesto = 100000000
            proyectoRegistrado.penalizacion = 10000000
            proyectoRegistrado.save()

            #Creacion de una fase para la modificacion
            faseRegistrada = fases()
            faseRegistrada.nombre = "fase Registrada"
            faseRegistrada.pk=2
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.estado = "creado"
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-05"
            faseRegistrada.fechaInicioR = "2014-03-06"
            faseRegistrada.presupuesto=100000000
            faseRegistrada.save()

            # Asignacion del permiso MOD para userRegistrado, a fin de poder modificar una fase
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "MOD"
            # permisoUserLogin.tipoObjeto = "fases"
            # permisoUserLogin.id_fk = 2
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login2', password='123')

        # Peticion POST para modificar la fase con id=2
        response = self.cliente.post("/fases/modificar/2",data={'nombre':'fase Registrada modificada'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'modificar'

        # Se consulta por el item modificado en la tabla items
        consultaInstancia = fases.objects.get(nombre="fase Registrada modificada")

        #print "\nNombre de la fase: ", consultaInstancia.nombre                  # Nombre de la fase modificada
        #print "Estado de la fase: ", consultaInstancia.estado                    # Estado de la fase modificada
        #print "Presupuesto: ", consultaInstancia.presupuesto                     # Presupuesto de la fase modificada


        self.assertNotEquals(consultaInstancia, None)


class TestEliminarFase(unittest.TestCase):
    """
        Prueba para comprobar la eliminacion de fases
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
            proyectoRegistrado.pk=3
            proyectoRegistrado.cantFases = 7
            proyectoRegistrado.fechaInicio = "2014-03-03"
            proyectoRegistrado.lider = userRegistrado
            proyectoRegistrado.fechaFinP = "2014-03-03"
            proyectoRegistrado.presupuesto= 1000
            proyectoRegistrado.penalizacion=500
            proyectoRegistrado.save()

            #Creacion de una fase para la eliminacion
            faseRegistrada = fases()
            faseRegistrada.nombre = "fase prueba"
            faseRegistrada.pk=3
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.estado = "creado"
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 1000
            faseRegistrada.save()

            # Asignacion del permiso DEL para userRegistrado, a fin de poder eliminar una fase
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "DEL"
            # permisoUserLogin.tipoObjeto = "fases"
            # permisoUserLogin.id_fk = 3
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login3', password='123')

        # Peticion POST para eliminar la fase con id=3
        response = self.cliente.post("/fases/eliminar/3",data={'comentario':'eliminacion fase de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        #Se consulta si la fase fue borrada, si su estado fue cambiado a 'eliminado'
        consultaInstancia = fases.objects.get(nombre="fase prueba", fechaInicioP="2014-03-24", estado="eliminado")


        #print "\nNombre de la fase: ", consultaInstancia.nombre                  # Nombre de la fase eliminada
        #print "Estado de la fase: ", consultaInstancia.estado                    # Estado de la fase eliminada
        #print "Presupuesto: ", consultaInstancia.presupuesto                     # Presupuesto de la fase eliminada

        self.assertNotEquals(consultaInstancia, None)


if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()