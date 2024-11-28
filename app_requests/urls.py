from django.urls import path
from . import views  # Importa tus vistas

urlpatterns = [
    path('', views.salon_index, name='salon_index'),
    path('create/', views.salon_create, name='lounge_create'),
    path('delete/<int:pk>/', views.salon_delete, name='lounge_delete'),
]
