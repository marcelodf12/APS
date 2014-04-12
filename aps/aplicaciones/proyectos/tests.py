"""
    Modulo de Test para el Modelo  Proyecto
"""
from django.utils import unittest
from aps.aplicaciones.proyectos.models import Proyectos
from datetime import datetime

class TestAltaProyecto(unittest.TestCase):
    """
        Test que simula un alta de Proyecto
    """
    def setUp(self):
        self.p1= Proyectos()
        self.p1.nombre = "P1"
        self.p1.fechaInicio = datetime.today()
        self.p1.cantFases = 1
        self.p1.estado = "creado"
        self.p1.save()
        self.p2= Proyectos()
        self.p2.nombre = "P2"
        self.p2.fechaInicio = datetime.today()
        self.p2.cantFases = 1
        self.p2.estado = "creado"
        self.p2.save()

    def test_details(self):
         self.assertEqual(self.p1.nombre, "P1")
         self.assertEqual(self.p2.nombre, "P2")

if __name__ == '__main__':
    unittest.main()