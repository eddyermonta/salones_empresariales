from django.db import models

# Create your models here.
class Client(models.Model):
    identification = models.CharField(max_length=20, unique=True)  # Identificación única
    first_name = models.CharField(max_length=50)  # Nombre
    last_name = models.CharField(max_length=50)  # Apellidos
    phone = models.CharField(max_length=15)  # Teléfono
    email = models.EmailField(unique=True)  # Correo
    department = models.CharField(max_length=50)  # Departamento
    city = models.CharField(max_length=50)  # Ciudad
    age = models.PositiveSmallIntegerField()  # Edad

    def __str__(self):
        return f"{self.first_name} {self.last_name}"