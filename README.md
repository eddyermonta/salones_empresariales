
# Proyecto de Gestión de Salones Empresariales

Este proyecto es una aplicación web construida con Django que permite gestionar la creación y eliminación de solicitudes de salones para eventos empresariales.

## Funcionalidades

- **Gestión de Clientes**: Crear, actualizar y listar clientes.
- **Solicitudes de Salones**: Crear, eliminar y listar solicitudes de salones para eventos empresariales.
- **Procedimientos Almacenados**: Utiliza procedimientos almacenados para insertar y eliminar clientes.
- **Filtrar Solicitudes Confirmadas**: Permite ver las solicitudes confirmadas dentro de un rango de fechas.

## Requisitos

- Python 3.x
- Django 3.x o superior
- PostgreSQL (u otra base de datos configurada en `settings.py`)
- Entorno virtual (opcional, recomendado)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/proyecto-salones.git
   cd proyecto-salones
   ```

2. Crear un entorno virtual (opcional pero recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Windows usa venv\Scripts\activate
    ```

3. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Ejecutar las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Cargar los datos iniciales (si es necesario):

    ```bash
    python manage.py loaddata data.json  # Si tienes datos iniciales en formato JSON
    ```

6. Crear un superusuario para acceder al panel de administración:

    ```bash
    python manage.py createsuperuser
    ```

7. Iniciar el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

   El servidor estará disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Estructura del Proyecto

```
    proyecto-salones/
    │
    ├── salon_requests/              # Aplicación de solicitudes de salones
    ├── clients/                     # Aplicación de gestión de clientes
    ├── templates/                   # Plantillas HTML
    ├── static/                      # Archivos estáticos (CSS, JS, imágenes)
    ├── manage.py                    # Archivo de gestión de Django
    ├── requirements.txt             # Dependencias del proyecto
    └── db.sqlite3                   # Base de datos (si usas SQLite)
```

## Comandos útiles

- **Iniciar el servidor de desarrollo**:

    ```bash
    python manage.py runserver
    ```

- **Ejecutar migraciones**:

    ```bash
    python manage.py migrate
    ```

