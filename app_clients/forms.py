from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    AGE_CHOICES = [(i, str(i)) for i in range(18, 101)]  # Opciones para la edad

    age = forms.ChoiceField(choices=AGE_CHOICES)  # Sobrescribimos el campo con una lista desplegable

    class Meta:
        model = Client
        fields = ['identification', 'first_name', 'last_name', 'phone', 'email', 'department', 'city', 'age']
