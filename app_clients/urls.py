from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_index, name='client_index'),  # Ruta para listar clientes
    path('client/create_or_update/', views.client_create_or_update, name='client_create_or_update'),
    path('client/create_or_update/<int:pk>/', views.client_create_or_update, name='client_create_or_update'),
    path('client/get/<int:pk>/', views.client_get, name='client_get')
]
