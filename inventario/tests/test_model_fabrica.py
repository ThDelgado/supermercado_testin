from inventario.models import Fabrica
 
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
 
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
class FabricaTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.fabrica = Fabrica(nombre = "Colgate")
        cls.fabrica.save()
 
    def test_model_content(self):
        """Nombre de la instancia / objeto corresponde al de la creación"""
        logger.info("Iniciando prueba: Nombre de la instancia / objeto corresponde al de la creación")
        self.assertEqual(self.fabrica.nombre, "Colgate")
       
    def test_verificacion_existencia(self):
        """Validar creación el DB de modelo fabrica"""
        logger.info("Iniciando prueba: creación el DB de modelo fabrica")
   
        fabrica = Fabrica.objects.get(id=self.fabrica.id)
        self.assertEqual(fabrica.nombre, self.fabrica.nombre)
       
 
 