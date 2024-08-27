# Biblioteca Online

## Descripción

Biblioteca Online es una aplicación Flask que permite a los usuarios gestionar un catálogo de libros. Los usuarios pueden añadir, eliminar, actualizar y consultar libros en una base de datos.

## Características

- **Agregar Libros**: Permite a los usuarios añadir libros a la base de datos.
- **Eliminar Libros**: Los usuarios pueden eliminar libros del catálogo.
- **Actualizar Libros**: Facilita la actualización de la información de los libros.
- **Consultar Libros**: Los usuarios pueden consultar la lista de libros disponibles y buscar por diferentes criterios.

## Tecnologías Utilizadas

- **Flask**: Un microframework para Python basado en Werkzeug, Jinja 2 y buenas intenciones.
- **SQLAlchemy**: ORM utilizado para interactuar con la base de datos.
- **MySQL**: Sistema de gestión de base de datos relacional.

## Estructura del Proyecto

\```
/BibliotecaOnline
|-- /application
|   |-- __init__.py
|   |-- /ports
|   |   |-- http_api.py
|   |-- /use_cases
|       |-- book_management.py
|-- /domain
|   |-- __init__.py
|   |-- /entities
|       |-- book.py
|-- /infrastructure
|   |-- __init__.py
|   |-- /database
|       |-- __init__.py
|       |-- models.py
|-- /tests
|   |-- __init__.py
|   |-- test_book_management.py
|-- docker-compose.yml
|-- Dockerfile
|-- requirements.txt
|-- README.md
\```

## Configuración del Entorno

### Prerrequisitos

- Python 3.8+
- pip
- virtualenv (opcional)
- Docker

### Instalación

1. **Clonar el Repositorio:**

   \```
   git clone https://github.com/usuario/BibliotecaOnline.git
   cd BibliotecaOnline
   \```

2. **Configurar el Entorno Virtual (Opcional):**

   \```
   python -m venv venv
   source venv/bin/activate  # En Windows use `venv\Scripts\activate`
   \```

3. **Instalar Dependencias:**

   \```
   pip install -r requirements.txt
   \```

4. **Configuración de Docker:**

   - Asegúrate de tener Docker y Docker Compose instalados.
   - Levanta los servicios:

   \```
   docker-compose up --build
   \```

### Uso

Para iniciar la aplicación, ejecuta:

\```
flask run
\```

La API estará disponible en `http://localhost:5001`.

### Endpoints

- **POST /books**: Añade un nuevo libro.
- **GET /books**: Lista todos los libros.
- **PUT /books/{id}**: Actualiza un libro específico.
- **DELETE /books/{id}**: Elimina un libro.

## Contribuir

Para contribuir al proyecto, considera lo siguiente:

1. **Fork el Repositorio**: Haz un 'fork' del proyecto a tu cuenta personal.
2. **Crea una Rama**: Crea una rama para cada característica o mejora.
3. **Haz tus Cambios**: Añade o cambia funcionalidades.
4. **Envía un Pull Request**: Para integrar tus cambios en el proyecto principal.

## Licencia

Este proyecto está bajo la Licencia MIT - vea el archivo [LICENSE.md](LICENSE) para detalles.
