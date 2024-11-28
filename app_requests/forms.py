from django import forms
from .models import SalonRequest

class SalonRequestForm(forms.ModelForm):
    class Meta:
        model = SalonRequest
        fields = ['client', 'event_date', 'number_of_people', 'reason', 'observations', 'status']
