// cargar modal
$('#clientModal').on('show.bs.modal', function(event) {
    var button = $(event.relatedTarget);
    var clientId = button.data('id');  // Obtener el ID del cliente
    var url = button.data('url');  // Obtener la URL desde el atributo data-url
    // Si es una actualización, se cargan los datos del cliente
    if (clientId) {
        $.ajax({
            url: url,  // Usar la URL correcta
            method: "GET",
            success: function(data) {
                $('#id_identification').val(data.identification);
                $('#id_first_name').val(data.first_name);
                $('#id_last_name').val(data.last_name);  // Nuevo campo: Apellidos
                $('#id_phone').val(data.phone);
                $('#id_email').val(data.email);
                $('#id_department').val(data.department);  // Nuevo campo: Departamento
                $('#id_city').val(data.city);
                $('#id_age').val(data.age);  // Nuevo campo: Edad

                $('#clientModalLabel').text('Actualizar Cliente');
                $('#clientForm').attr('data-id', clientId); 
            }
        });
    } else {
        // Si es una creación, se limpia el formulario
        $('#clientForm')[0].reset();
        $('#clientModalLabel').text('Crear Cliente');
    }
});


// Enviar el formulario mediante AJAX (crear o actualizar) guardar
$('#clientForm').on('submit', function(e) {
    e.preventDefault();
    var formData = $(this).serialize(); 
    var clientId = $(this).attr('data-id');  // Obtener el ID del cliente si existe
    var url = clientCreateOrUpdateUrl; // URL para creación
    if (clientId !== undefined) {
        url +=clientId+"/";  // URL para actualización
    }

    $.ajax({
        type: 'POST',
        url: url,
        data: formData,
        success: function(response) {
            $('#clientModal').modal('hide'); 
            alert('Cliente guardado exitosamente');
            location.reload();  
        },
        error: function(xhr, status, error) {
            alert('Error al guardar los datos. Por favor intente nuevamente.');
        }
    });
});
