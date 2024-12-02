from inventario.models import Producto
 
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
 
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
class ProductoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.producto = Producto(nombre = "Shampoo")
        cls.producto.save()
 
    def test_model_content(self):
        """Nombre de la instancia / objeto corresponde al de la creación"""
        logger.info("Iniciando prueba: Nombre de la instancia / objeto corresponde al de la creación")
        self.assertEqual(self.producto.nombre, "Shampoo")
       
    def test_verificacion_existencia(self):
        """Validar creación el DB de modelo producto"""
        logger.info("Iniciando prueba: creación el DB de modelo producto")
   
        producto = Producto.objects.get(id=self.producto.id)
        self.assertEqual(producto.nombre, self.producto.nombre)
       
 
 