from django.db import models


class Producto(models.Model):
    class Categoria(models.TextChoices):
        LAPTOPS = "laptops", "Laptops"
        AUDIO = "audio", "Audio"
        ACCESORIOS = "accesorios", "Accesorios"
        MONITORES = "monitores", "Monitores"

    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=220)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=Categoria.choices)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.CharField(max_length=80, default="producto.svg")
    destacado = models.BooleanField(default=False)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
