from domain.entities.book import Book
from infrastructure.repository.book_repository import BookRepository
import logging

class BookManagement:
    def __init__(self):
        self.book_repository = BookRepository()

    def add_book(self, data):
        """
        Create a new book and save it to the database.

        :param data: A dictionary with the book's details (title, author, ISBN).
        :return: Dictionary with information on the added book or an error.
        """
        new_book = Book(data['title'], data['author'], data['isbn'])
        result, error_message = self.book_repository.add(new_book)
        if result:
            return {'status': 'success', 'book': data}
        else:
            # Provides the actual error message to assist in debugging
            return {'status': 'error', 'message': error_message or 'Failed to add book'}

    def remove_book(self, book_id):
        """
        Remove a book from the database by its ID.

        :param book_id: ID of the book to remove.
        :return: Dictionary indicating success or failure.
        """
        result = self.book_repository.remove(book_id)
        if result:
            return {'status': 'success', 'message': 'Book successfully removed'}
        else:
            return {'status': 'error', 'message': 'Failed to remove book'}

    def update_book(self, book_id, data):
        """
        Updates the details of an existing book.

        :param book_id: ID of the book to update.
        :param data: Dictionary with the new book data.
        :return: Dictionary indicating success or failure.
        """
        result = self.book_repository.update(book_id, data)
        if result:
            return {'status': 'success', 'message': 'Book updated successfully'}
        else:
            return {'status': 'error', 'message': 'Failed to update book'}

    def get_book(self, book_id):
        """
        Retrieves the details of a book by its ID.

        :param book_id: ID of the book.
        :return: Book instance or None.
        """
        book = self.book_repository.get(book_id)
        return book

    def list_books(self):
        """
        Lists all the books in the database.

        :return: List of book instances or an error message.
        """
        try:
            books = self.book_repository.list_all()
            print(books)
            return {'status': 'success', 'data': books}
        except Exception as e:
            logging.error(f"Unexpected error when listing books: {e}")
            return {'status': 'error', 'message': 'An unexpected error occurred while retrieving books'}
