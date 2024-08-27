from domain.entities.book import Book
from infrastructure.repository.book_repository import BookRepository
import logging

class BookManagement:
    def __init__(self):
        self.book_repository = BookRepository()

    def add_book(self, data):
        """
        Crea un nuevo libro y lo guarda en la base de datos.

        :param data: Un diccionario con los datos del libro (título, autor, ISBN).
        :return: Diccionario con información del libro agregado o error.
        """
        new_book = Book(data['title'], data['author'], data['isbn'])
        result, error_message = self.book_repository.add(new_book)
        if result:
            return {'status': 'success', 'book': data}
        else:
            # Proporciona el mensaje de error real para ayudar en la depuración
            return {'status': 'error', 'message': error_message or 'No se pudo agregar el libro'}

    def remove_book(self, book_id):
        """
        Elimina un libro de la base de datos por ID.

        :param book_id: ID del libro a eliminar.
        :return: Diccionario indicando éxito o fracaso.
        """
        result = self.book_repository.remove(book_id)
        if result:
            return {'status': 'success', 'message': 'Libro eliminado correctamente'}
        else:
            return {'status': 'error', 'message': 'No se pudo eliminar el libro'}

    def update_book(self, book_id, data):
        """
        Actualiza los detalles de un libro existente.

        :param book_id: ID del libro a actualizar.
        :param data: Diccionario con los nuevos datos del libro.
        :return: Diccionario indicando éxito o fracaso.
        """
        result = self.book_repository.update(book_id, data)
        if result:
            return {'status': 'success', 'message': 'Libro actualizado correctamente'}
        else:
            return {'status': 'error', 'message': 'No se pudo actualizar el libro'}

    def get_book(self, book_id):
        """
        Obtiene los detalles de un libro por su ID.

        :param book_id: ID del libro.
        :return: Instancia del libro o None.
        """
        book = self.book_repository.get(book_id)
        return book

    def list_books(self):
        """
        Lista todos los libros en la base de datos.

        :return: Lista de instancias de libros o un mensaje de error.
        """
        try:
            books = self.book_repository.list_all()
            print(books)
            return {'status': 'success', 'data': books}
        except Exception as e:
            logging.error(f"Unexpected error when listing books: {e}")
            return {'status': 'error', 'message': 'An unexpected error occurred while retrieving books'}
