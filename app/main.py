from flask import Flask
from application.ports.http_api import init_app
from infrastructure.database import init_db  # Asegúrate de tener esta importación correcta


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    init_db(app)  # Inicializa la base de datos aquí
    init_app(app)  # Inicializa otras partes de la aplicación

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Especifica el puerto si es necesario
