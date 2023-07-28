from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

# Create your tests here.

class LaboratorioTests(TestCase):
    databases="__all__"
    @classmethod 
    
    def setUpTestData(cls): 
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio prueba', 
            ciudad ='Ciudad prueba', 
            pais ='Pais prueba'
            )
    
    def test_model_content(self): 
        self.assertEqual(self.laboratorio.nombre, "Laboratorio prueba") 
        self.assertEqual(self.laboratorio.ciudad, "Ciudad prueba")
        self.assertEqual(self.laboratorio.pais, "Pais prueba")

    def test_url_exists_at_correct_location(self): 
        response = self.client.get("/") 
        self.assertEqual(response.status_code, 200)

    def test_homepage(self): 
        response = self.client.get(reverse("mostrar")) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "mostrar.html") 
        self.assertContains(response, "Informacion de laboratorios")