from django.core.management.base import BaseCommand
from catalogo.models import Producto


PRODUCTOS = [
    ("NexoBook Air 14", "Rendimiento ligero para trabajar y crear desde cualquier lugar.", "4299.00", "laptops", 8, "laptop.svg", True),
    ("Aurora Headphones", "Audio envolvente y comodidad que acompaña todo el día.", "649.00", "audio", 15, "headphones.svg", True),
    ("Nexo Studio Display", "Una nueva perspectiva para tus ideas y proyectos.", "1899.00", "monitores", 6, "monitor.svg", True),
    ("Teclado Forma 75", "Precisión y tacto suave en un diseño compacto.", "389.00", "accesorios", 12, "keyboard.svg", False),
    ("Mouse Trazo Pro", "Control preciso y ergonomía para cada jornada.", "219.00", "accesorios", 18, "mouse.svg", False),
    ("Pulse Mini Speaker", "Sonido claro y potente en formato portátil.", "329.00", "audio", 9, "speaker.svg", False),
    ("NexoBook Pro 16", "Potencia y espacio de trabajo para proyectos exigentes.", "5999.00", "laptops", 4, "laptop.svg", False),
    ("Cámara Enfoque HD", "Imagen nítida para clases, reuniones y transmisiones.", "279.00", "accesorios", 0, "camera.svg", False),
]


class Command(BaseCommand):
    help = "Carga una colección de demostración sin crear duplicados."

    def handle(self, *args, **options):
        for nombre, descripcion, precio, categoria, stock, imagen, destacado in PRODUCTOS:
            Producto.objects.update_or_create(nombre=nombre, defaults={
                "descripcion": descripcion, "precio": precio, "categoria": categoria,
                "stock": stock, "imagen": imagen, "destacado": destacado,
            })
        self.stdout.write(self.style.SUCCESS(f"Colección lista: {Producto.objects.count()} productos."))
