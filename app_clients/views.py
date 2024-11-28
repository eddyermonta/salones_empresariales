from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Client
from .forms import ClientForm

# Vista para la página principal de clientes
def client_index(request):
    clients = Client.objects.all()  # Obtiene todos los clientes
    return render(request, 'clients/client_index.html', {'clients': clients})

def client_create_or_update(request, pk=None):
    if request.method == 'POST':
        if pk:
            client = get_object_or_404(Client, pk=pk)
        else:
            client = Client()

        form = ClientForm(request.POST, instance=client)
        print(form.errors)
        if form.is_valid():
            client = form.save()
            return JsonResponse({
                'id': client.pk,
                'identification': client.identification,
                'first_name': client.first_name,
                'last_name': client.last_name,
                'phone': client.phone,
                'email': client.email,
                'department': client.department,
                'city': client.city,
                'age': client.age
            })
        else:
            return JsonResponse({'error': 'Form is not valid', 'errors': form.errors}, status=400)
    else:
        form = ClientForm()

    return render(request, 'clients/client_form_modal.html', {'form': form})


def client_get(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return JsonResponse({
        'identification': client.identification,
        'first_name': client.first_name,
        'last_name': client.last_name,  # Nuevo campo: Apellidos
        'phone': client.phone,
        'email': client.email,
        'department': client.department,  # Nuevo campo: Departamento
        'city': client.city,
        'age': client.age,  # Nuevo campo: Edad
    })