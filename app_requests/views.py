
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from app_clients.models import Client
from .models import SalonRequest
from .forms import SalonRequestForm

def salon_index(request):
    clients = Client.objects.all()
    salon_requests = SalonRequest.objects.all()
    return render(request, 'lounge/lounge_index.html', {
        'clients': clients,
        'salon_requests': salon_requests,
    })

def salon_create(request):
    if request.method == 'POST':
        form = SalonRequestForm(request.POST)
        if form.is_valid():
            salon_request = form.save()  # Guardar la nueva solicitud
            return JsonResponse({'message': 'Solicitud creada exitosamente'})
        else:
            return JsonResponse({'error': 'Formulario inválido'}, status=400)
    else:
        form = SalonRequestForm()

    return render(request, 'salons/salon_form_modal.html', {'form': form})

def salon_delete(request, pk):
    if request.method == 'POST':
        salon_request = get_object_or_404(SalonRequest, pk=pk)
        salon_request.delete()  # Eliminar la solicitud
        return JsonResponse({'message': 'Solicitud eliminada exitosamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=405)