from django.db import models

from app_clients.models import Client

# Create your models here.
class SalonRequest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="salon_requests")
    event_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    reason = models.CharField(
        max_length=50,
        choices=[
            ('Evento empresarial', 'Evento empresarial'),
            ('Despedida empresa', 'Despedida empresa'),
            ('Desayuno comercial', 'Desayuno comercial'),
            ('Almuerzo', 'Almuerzo'),
        ]
    )
    observations = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Confirmado', 'Confirmado'),
            ('No confirmado', 'No confirmado'),
        ],
        default='No confirmado'
    )