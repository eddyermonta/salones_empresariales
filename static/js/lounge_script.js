$('#salonForm').on('submit', function(e) {
    e.preventDefault();  // Prevenir el envío normal del formulario
    alert('Formulario enviado');  // Mostrar un mensaje de alerta

    var formData = $(this).serialize();  // Obtener los datos del formulario

    var url = loungeCreate;  // La URL para crear la solicitud (puede ser una URL que usas para crear una solicitud)

    $.ajax({
        type: 'POST',  // Asegurarse de que se está enviando como POST
        url: url,
        data: formData,
        success: function(response) {
            alert('Solicitud guardada exitosamente');
            location.reload();  // Recargar la página para reflejar los cambios
        },
        error: function(xhr, status, error) {
            alert('Error al guardar la solicitud.');
        }
    });
});


// Lógica para manejar la eliminación de la solicitud
$('.deleteSalonBtn').on('click', function(event) {
    event.preventDefault();  // Evitar que el enlace redirija a otro lugar

    var salonId = $(this).data('id');  // Obtener el ID de la solicitud de salón
    var url = $(this).data('url');  // Obtener la URL de eliminación

    // Confirmar con el usuario antes de eliminar
    if (confirm('¿Está seguro de que desea eliminar esta solicitud?')) {
        // Enviar la solicitud de eliminación con AJAX
        $.ajax({
            type: 'POST',
            url: url,  // URL para la eliminación
            data: {
                'salon_id': salonId,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()  // Asegúrate de incluir el token CSRF
            },
            success: function(response) {
                alert('Solicitud eliminada exitosamente');
                $('a[data-id="' + salonId + '"]').closest('tr').remove();
            },
            error: function(xhr, status, error) {
                alert('Error al eliminar la solicitud. Por favor intente nuevamente.');
            }
        });
    }
});
