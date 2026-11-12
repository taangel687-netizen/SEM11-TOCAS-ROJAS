from django.test import TestCase
from django.urls import reverse
from .models import Producto


class CatalogoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Producto.objects.create(nombre="Aurora", descripcion="Audífonos", precio="199.00", categoria="audio", stock=4, imagen="headphones.svg", destacado=True)
        Producto.objects.create(nombre="Trazo", descripcion="Mouse", precio="59.00", categoria="accesorios", stock=0, imagen="mouse.svg")

    def test_bienvenida_y_catalogo(self):
        self.assertEqual(self.client.get(reverse("catalogo:inicio")).status_code, 200)
        response = self.client.get(reverse("catalogo:lista"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aurora")
        self.assertContains(response, "Trazo")

    def test_filtro_y_busqueda(self):
        response = self.client.get(reverse("catalogo:lista"), {"categoria": "audio", "q": "auro"})
        self.assertContains(response, "Aurora")
        self.assertNotContains(response, "Trazo")
        self.assertContains(self.client.get(reverse("catalogo:lista"), {"q": "inexistente"}), "No encontramos productos")
