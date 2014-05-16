"""
    Modulo de Pruebas Unitarias para la aplicacion items
"""

from django.utils import unittest
from django.contrib.auth.models import User
from django.test.client import Client

from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.items.models import items, atributo, relacion


# Create your tests here.
class TestCrearItem(unittest.TestCase):
    """ Prueba para comprobar la creacion de items """

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
            #???????????????????????????????????????????
            faseRegistrada.orden = 1
            faseRegistrada.save()


    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login', password='123')

        # Peticion POST para crear un item con id=1
        response = self.cliente.post("/items/crear/1",data={'nombre':'item prueba',
                                                            'complejidad':'5',
                                                            'costo':'2000'
                                                            })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

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
            #???????????????????????????????????????????
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de un item para la modificacion
            itemRegistrado = items()
            itemRegistrado.pk = 2
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()


    def test_details(self):
        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login2', password='123')

        # Peticion POST para modificar el item con id=2
        response = self.cliente.post("/items/modificar/2",data={'nombre':'item prueba modificado',
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
        Prueba para comprobar la eliminacion logica de items
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
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000
            #???????????????????????????????????????????
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de un item para la eliminacion
            itemRegistrado = items()
            itemRegistrado.pk = 3
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()

            # Asignacion del permiso DEL para userRegistrado, a fin de poder eliminar un item
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "DEL"
            # permisoUserLogin.tipoObjeto = "item"
            # permisoUserLogin.id_fk = 3
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login3', password='123')

        # Peticion POST para eliminar el item con id=3
        response = self.cliente.post("/items/eliminar/3",data={'comentario':'eliminacion item de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        #Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
        consultaInstancia = items.objects.get(nombre="item Registrado", complejidad=10, versionAct=1, estado="eliminado" )


        # print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item borrado
        # print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item borrado
        # print "Version actual:", consultaInstancia.versionAct                     # Version actual del item borrado
        # print "Estado del item:", consultaInstancia.estado                        # Estado del item borrado

        self.assertNotEquals(consultaInstancia, None)

class TestCrearAtributo(unittest.TestCase):
    """
        Prueba para comprobar la creacion de atributos
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
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000
            #???????????????????????????????????????????
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de un item para instanciar el atributo
            itemRegistrado = items()
            itemRegistrado.pk = 4
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()

            # Asignacion del permiso DEL para userRegistrado, a fin de poder eliminar un item
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "DEL"
            # permisoUserLogin.tipoObjeto = "item"
            # permisoUserLogin.id_fk = 3
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login4', password='123')

        # Peticion POST para agregar un atributo al item con id=4
        response = self.cliente.post("/items/atributos/agregar/4",data={'nombre':'atributo de prueba',
                                                                        'descripcion':'creacion atributo de prueba'
                                                                })

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        #Se consulta por el atributo creado
        consultaInstancia = atributo.objects.get(nombre="atributo de prueba", descripcion="creacion atributo de prueba")


        #print "\nNombre del Atributo: ", consultaInstancia.nombre                    # Nombre del atributo creado
        #print "Descripcion del Atributo: ", consultaInstancia.descripcion            # Descripcion del atributo creado

        self.assertNotEquals(consultaInstancia, None)


# class TestModificarAtributo(unittest.TestCase):
#     """
#         Prueba para comprobar la modificacion de atributos
#     """
#     def setUp(self):
#
#             # Creacion de un cliente
#             self.cliente = Client()
#
#             # Creacion de un usuario para la autenticacion
#             self.userLogin = User.objects.create_user(username="fulano Login5", password="123")
#
#             #Creacion de un usuario Lider para instanciar un proyecto
#             userRegistrado = User()
#             userRegistrado.username = "fulano Lider5"
#             userRegistrado.password = "123"
#             userRegistrado.save()
#
#             #Creacion de un proyecto para instanciar una fase
#             proyectoRegistrado = Proyectos()
#             proyectoRegistrado.cantFases = 7
#             proyectoRegistrado.fechaInicio = "2014-03-03"
#             proyectoRegistrado.lider = userRegistrado
#             proyectoRegistrado.fechaFinP = "2014-10-03"
#             proyectoRegistrado.fechaFinR = "2014-10-04"
#             proyectoRegistrado.presupuesto=1500
#             proyectoRegistrado.penalizacion=350
#             proyectoRegistrado.save()
#
#             #Creacion de una fase para instanciar un item
#             faseRegistrada = fases()
#             faseRegistrada.nombre = "fase Registrada"
#             faseRegistrada.versionAct = 1
#             faseRegistrada.complejidad = 10
#             faseRegistrada.cantItems = 6
#             faseRegistrada.fechaInicio = "2014-03-24"
#             faseRegistrada.fechaInicioP = "2014-03-24"
#             faseRegistrada.fechaInicioR = "2014-03-24"
#             faseRegistrada.presupuesto = 2500000
#             #???????????????????????????????????????????
#             faseRegistrada.orden = 1
#             faseRegistrada.save()
#
#             #Creacion de un item
#             itemRegistrado = items()
#             itemRegistrado.pk = 5
#             itemRegistrado.nombre = "item Registrado"
#             itemRegistrado.fase = faseRegistrada
#             itemRegistrado.versionAct = 1
#             itemRegistrado.complejidad = 10
#             itemRegistrado.costo = 2000
#             itemRegistrado.save()
#
#             # Asignacion del permiso DEL para userRegistrado, a fin de poder eliminar un item
#             # permisoUserLogin = Permisos()
#             # permisoUserLogin.permiso = "DEL"
#             # permisoUserLogin.tipoObjeto = "item"
#             # permisoUserLogin.id_fk = 3
#             # permisoUserLogin.usuario = userRegistrado
#             # permisoUserLogin.save()
#
#
#     def test_details(self):
#
#         # Cliente es autenticado como el usuario 'fulano Login'
#         b = self.cliente.login(username='fulano Login3', password='123')
#
#         # Peticion POST para agregar un atributo con al item con id=1
#         response = self.cliente.post("/items/atributos/agregar/5",data={'nombre':'atributo de prueba',
#                                                                         'descripcion':'creacion atributo de prueba'
#                                                                 })
#
#         print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'
#
#         #Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
#         consultaInstancia = atributo.objects.get(nombre="atributo de prueba", descripcion="creacion atributo de prueba")
#
#
#         #print "\nNombre del Atributo: ", consultaInstancia.nombre                    # Nombre del atributo creado
#         #print "Descripcion del Atributo: ", consultaInstancia.descripcion            # Descripcion del atributo creado
#
#         self.assertNotEquals(consultaInstancia, None)


class TestCrearRelacion(unittest.TestCase):
    """
        Prueba para comprobar la creacion de relaciones
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            self.userLogin = User.objects.create_user(username="fulano Login5", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider5"
            userRegistrado.password = "123"
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
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
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000
            #???????????????????????????????????????????
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de un item
            itemRegistrado = items()
            itemRegistrado.pk = 5
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()

            # Asignacion del permiso DEL para userRegistrado, a fin de poder eliminar un item
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "DEL"
            # permisoUserLogin.tipoObjeto = "item"
            # permisoUserLogin.id_fk = 3
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login5', password='123')

        # Peticion POST para agregar una relacion al item con id=5
        response = self.cliente.post("/items/relaciones/listarParaCrear/5")

        #AQUI SE TIENE EL COMBOBOX DE RELACIONES, NO ENTIENDO COMO CREA
        #NO SE COMO ELEGIR UNA OPCION DE UN COMBOBOX

        print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'crear'

        #Se consulta por la relacion creada
        #consultaInstancia = relacion.objects.get(itemHijo_id="", itemPadre_id="", estado="")


        #print "\nItem Hijo: ", consultaInstancia.itemHijo_id                    # ID del item hijo
        #print "\nItem Padre: ", consultaInstancia.itemPadre_id                  # ID del item padre

        #self.assertNotEquals(consultaInstancia, None)

class TestEliminarRelaciones(unittest.TestCase):
    """
        Prueba para comprobar la eliminacion logica de relaciones
    """
    def setUp(self):

            # Creacion de un cliente
            self.cliente = Client()

            # Creacion de un usuario para la autenticacion
            self.userLogin = User.objects.create_user(username="fulano Login6", password="123")

            #Creacion de un usuario Lider para instanciar un proyecto
            userRegistrado = User()
            userRegistrado.username = "fulano Lider6"
            userRegistrado.password = "123"
            userRegistrado.save()

            #Creacion de un proyecto para instanciar una fase
            proyectoRegistrado = Proyectos()
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
            faseRegistrada.versionAct = 1
            faseRegistrada.complejidad = 10
            faseRegistrada.cantItems = 6
            faseRegistrada.fechaInicio = "2014-03-24"
            faseRegistrada.fechaInicioP = "2014-03-24"
            faseRegistrada.fechaInicioR = "2014-03-24"
            faseRegistrada.presupuesto = 2500000
            #???????????????????????????????????????????
            faseRegistrada.orden = 1
            faseRegistrada.save()

            #Creacion de un item
            itemRegistrado = items()
            itemRegistrado.pk = 6
            itemRegistrado.nombre = "item Registrado"
            itemRegistrado.fase = faseRegistrada
            itemRegistrado.versionAct = 1
            itemRegistrado.complejidad = 10
            itemRegistrado.costo = 2000
            itemRegistrado.save()

            # Asignacion del permiso DEL para userRegistrado, a fin de poder eliminar un item
            # permisoUserLogin = Permisos()
            # permisoUserLogin.permiso = "DEL"
            # permisoUserLogin.tipoObjeto = "item"
            # permisoUserLogin.id_fk = 3
            # permisoUserLogin.usuario = userRegistrado
            # permisoUserLogin.save()


    def test_details(self):

        # Cliente es autenticado como el usuario 'fulano Login'
        b = self.cliente.login(username='fulano Login6', password='123')

        # Peticion POST para eliminar el item con id=3
        # PRIMERO TENGO QUE SABER CREAR UNA RELACION
        #response = self.cliente.post("/items/relaciones/eliminar/",data={'comentario':'eliminacion item de prueba'})

        #print response.__str__()                           # Muestra la URL a la que se redirecciona luego de 'borrar'

        #Se consulta si el item fue borrado, si su estado fue cambiado a 'eliminado'
        #consultaInstancia = items.objects.get(nombre="item Registrado", complejidad=10, versionAct=1, estado="eliminado" )


        # print "\nNombre del item: ", consultaInstancia.nombre                     # Nombre del item borrado
        # print "Complejidad del item: ", consultaInstancia.complejidad             # Complejidad del item borrado
        # print "Version actual:", consultaInstancia.versionAct                     # Version actual del item borrado
        # print "Estado del item:", consultaInstancia.estado                        # Estado del item borrado

        #self.assertNotEquals(consultaInstancia, None)


if __name__ == '__main__':

    #Se ejecuta la prueba unitaria
    unittest.main()
