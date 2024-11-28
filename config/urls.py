
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from config.views import home  # Solo para una vista rápida


def favicon_view(request):
    return HttpResponse(status=204)  # Responde con éxito vacío (sin contenido)

urlpatterns = [
    path('', home, name='home'),  # Ruta raíz
    path('admin/', admin.site.urls),
    path('favicon.ico', favicon_view),  # Maneja la solicitud del favicon
    path('clients/', include('app_clients.urls')),  # Rutas de clientes
    path('lounge/', include('app_requests.urls')),  # Rutas de solicitudes
]
