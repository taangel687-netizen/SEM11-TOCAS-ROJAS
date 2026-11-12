# Nexo Tech — Catálogo de productos tecnológicos

Repositorio: https://github.com/taangel687-netizen/SEM11-TOCAS-ROJAS

Proyecto de la práctica grupal de la semana 11, Desarrollo de Aplicaciones Web (UNCP). Desarrollado por **Rojas Cerron Zair** y **Tocas Anglas Angel**.

## Puesta en marcha

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_productos
python manage.py check
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` o `http://127.0.0.1:8000/catalogo/`. La carga de productos se puede repetir sin duplicar registros. SQLite se genera localmente y no se incluye en Git.

## Arquitectura MTV

```text
Request → config/urls.py → catalogo/urls.py → View
                                            │
                                            ├── Model / ORM → SQLite
                                            │
                                            └── Template → Response HTML
```

- `/`: función `bienvenida` (FBV), contexto con tres productos destacados y el total.
- `/catalogo/`: clase `CatalogoView` (`ListView`), búsqueda por nombre y filtro por categoría.
- `Producto`: nombre, descripción, precio, categoría, stock, imagen y destacado.
- `base.html`: estructura común; `inicio.html` y `catalogo.html`: herencia y bloques.

## Dos QuerySets utilizados

```python
Producto.objects.filter(destacado=True, stock__gt=0).order_by("nombre")[:3]
Producto.objects.filter(categoria="audio", nombre__icontains="Aurora").order_by("-destacado", "nombre")
```

El primero reúne destacados disponibles para la portada. El segundo representa los filtros combinados del catálogo. Un `QuerySet` es *lazy*: construirlo o encadenar `filter()` y `order_by()` no ejecuta SQL inmediatamente. La consulta ocurre cuando se itera en la plantilla, se convierte con `list()` o se evalúa con `count()`, entre otras operaciones. Esto permite componer condiciones antes de acceder a la base de datos.

## Plantillas

`{% extends %}` y `{% block %}` reutilizan la estructura común. `{% for %}` recorre productos y categorías; `{% if %}` controla disponibilidad, destacado y estados vacíos; `{% url %}` crea enlaces por nombre. Los filtros `truncatechars`, `floatformat`, `length`, `pluralize`, `upper` y `urlencode` ajustan la presentación. La interfaz responde a escritorio y móvil.

## Trabajo de los integrantes

| Integrante | Responsabilidad principal | Evidencia en el código |
|---|---|---|
| Rojas Cerron Zair | Arquitectura Django, modelo, migraciones y consultas ORM | `config/`, `catalogo/models.py`, `catalogo/migrations/`, comando de carga |
| Tocas Anglas Angel | FBV y CBV, plantillas, estilos y experiencia responsive | `catalogo/views.py`, `catalogo/urls.py`, `templates/`, `static/` |
| Ambos | Integración, documentación y validación | `README.md`, informe, `manage.py check` y pruebas de navegación |

## Evidencias

Las capturas de la página principal, catálogo y estructura están en `evidencias/`. El informe técnico en PDF está en esta carpeta.

## Validación

Ejecutar `python manage.py check` y `python manage.py test`. Para producción, configurar `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` y `DJANGO_ALLOWED_HOSTS`; la clave incluida es solo para desarrollo local.


