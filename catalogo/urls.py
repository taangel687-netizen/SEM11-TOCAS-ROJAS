from django.urls import path
from .views import CatalogoView, bienvenida

app_name = "catalogo"
urlpatterns = [
    path("", bienvenida, name="inicio"),
    path("catalogo/", CatalogoView.as_view(), name="lista"),
]
