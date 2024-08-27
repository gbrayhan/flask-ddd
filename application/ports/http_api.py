from flask import jsonify, request
from application.use_cases.book_management import BookManagement

def init_app(app):
    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        book_management = BookManagement()
        result = book_management.add_book(data)
        return jsonify(result), 201

    @app.route('/', methods=['GET'])
    def home():
        """
        Ruta raíz que devuelve un mensaje de bienvenida.
        """
        return jsonify({'message': 'Bienvenido a la Biblioteca Online'}), 200
