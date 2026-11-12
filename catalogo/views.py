from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


def bienvenida(request):
    destacados = Producto.objects.filter(destacado=True, stock__gt=0).order_by("nombre")[:3]
    return render(request, "inicio.html", {
        "destacados": destacados,
        "total_productos": Producto.objects.count(),
    })


class CatalogoView(ListView):
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        queryset = Producto.objects.all()
        categoria = self.request.GET.get("categoria", "").strip().lower()
        if categoria in Producto.Categoria.values:
            queryset = queryset.filter(categoria=categoria)
        busqueda = self.request.GET.get("q", "").strip()
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset.order_by("-destacado", "nombre")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Producto.Categoria.choices
        context["categoria_actual"] = self.request.GET.get("categoria", "").strip().lower()
        context["busqueda"] = self.request.GET.get("q", "").strip()
        context["total_catalogo"] = Producto.objects.count()
        context["disponibles"] = Producto.objects.filter(stock__gt=0).count()
        return context
