from django.test import TestCase
from django.urls import reverse
 
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
class ProductoViewTests(TestCase):
   
    @classmethod
    def setUpTestData(cls):
       pass
       
    def test_page_producto(self):
        """Verificador código respuesta HTTP 200 de vista posts"""
        logger.info("Iniciando prueba: Verificación código respuesta HTTP 200 en vista posts.")
       
        response = self.client.get(reverse("listado_productos"))
        self.assertEqual(response.status_code, 200, "Código de respueta de la vista no coincide con el código 200")


