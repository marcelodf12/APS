"""
    Modulo de Pruebas Unitarias para la aplicacion fases
"""

from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from aps.aplicaciones.fases.models import fases, Proyectos
from aps.aplicaciones.items.models import items



# Create your tests here.
class TestCrearFase(unittest.TestCase):
    """ Prueba para comprobar la creacion de fases """

    def setUp(self):
            """
                Metodo de inicializacion
            """

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



    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear una fase
        response = self.cliente.post("/fases/crearEnProyecto/1",data={'nombre':'fase prueba',
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
        response = self.cliente.post("/fases/modificar/2",data={'nombre':'fase Registrada modificada',
                                                                'presupuesto':'20000000'
                                                          })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'modificar'

        # Se consulta por el item modificado en la tabla items
        consultaInstancia = fases.objects.get(nombre="fase Registrada modificada", presupuesto="20000000")

        #print "\nNombre de la fase: ", consultaInstancia.nombre                  # Nombre de la fase modificada
        #print "Estado de la fase: ", consultaInstancia.estado                    # Estado de la fase modificada
        #print "Presupuesto: ", consultaInstancia.presupuesto                     # Presupuesto de la fase modificada


        self.assertNotEquals(consultaInstancia, None)


class TestFinalizarFase(unittest.TestCase):
    """
        Prueba para comprobar la eliminacion de fases
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            self.userLogin = User.objects.create_user(username="fulano Login4", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider4"
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

            #Creacion de una fase con orden = 1
            faseRegistrada = fases()
            faseRegistrada.pk=4
            faseRegistrada.nombre = "fase prueba terminar"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-25"
            faseRegistrada.estado = "creado"
            faseRegistrada.proyecto = proyectoRegistrado
            faseRegistrada.costo = 100
            faseRegistrada.cantItems = 6
            faseRegistrada.presupuesto = 1000
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de un item (ya con estado finalizado)
            itemRegistrado = items()
            itemRegistrado.pk = 10
            itemRegistrado.nombre = "item Registrado10"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.estado = 'finalizado'
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login4', password='123')

        # Peticion POST para finalizar la fase con id=4
        response = self.cliente.post("/fases/finalizar/4",data={'comentario':'prueba finalizacion de fase'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        #Se consulta si la fase fue finalizada
        consultaInstancia = fases.objects.get(nombre="fase prueba terminar", fechaInicioP="2014-03-24", estado="finalizada")


        #print "\nNombre de la fase: ", consultaInstancia.nombre                  # Nombre de la fase eliminada
        #print "Estado de la fase: ", consultaInstancia.estado                    # Estado de la fase eliminada
        #print "Presupuesto: ", consultaInstancia.presupuesto                     # Presupuesto de la fase eliminada

        self.assertNotEquals(consultaInstancia, None)


if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()