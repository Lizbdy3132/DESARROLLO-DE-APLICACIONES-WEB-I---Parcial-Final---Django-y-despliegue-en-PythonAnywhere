from django.test import TestCase
from django.urls import reverse
from .models import Programa


class ProgramaTests(TestCase):
    def test_mostrar_formulario(self):
        respuesta = self.client.get(reverse("crear_programa"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Registrar programa")

    def test_guardar_programa(self):
        respuesta = self.client.post(reverse("crear_programa"), {
            "codigo": "SIS01",
            "nombre": "Ingeniería de Sistemas",
            "estado": "on",
            "facultad": "Ingeniería",
        })
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(Programa.objects.filter(codigo="SIS01").exists())

    def test_codigo_no_se_repite(self):
        Programa.objects.create(codigo="SIS01", nombre="Sistemas", facultad="Ingeniería")
        respuesta = self.client.post(reverse("crear_programa"), {
            "codigo": "SIS01",
            "nombre": "Otro programa",
            "facultad": "Ingeniería",
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Programa.objects.count(), 1)
