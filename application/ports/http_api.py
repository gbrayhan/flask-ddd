from flask import jsonify, request
from application.use_cases.book_management import BookManagement

def init_app(app):
    @app.route('/books', methods=['POST'])
    def add_book():
        data = request.get_json()
        book_management = BookManagement()
        result = book_management.add_book(data)
        return jsonify(result), 201

    @app.route('/books', methods=['GET'])
    def list_books():
        book_management = BookManagement()
        books = book_management.list_books()
        print("final books", books)
        if books['status'] == 'success':
            return jsonify({'status': 'success', 'data': [book.to_dict() for book in books['data']]})
        else:
            return jsonify(books), 400

    @app.route('/', methods=['GET'])
    def home():
        """
        Root route that returns a welcome message.
        """
        return jsonify({'message': 'Welcome to the Online Library'}), 200
