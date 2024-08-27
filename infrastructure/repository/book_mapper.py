# infrastructure/repository/book_mapper.py

from domain.entities.book import Book
from .models import BookDTO

class BookMapper:
    @staticmethod
    def to_domain(book_dto):
        """ Mapea BookDTO a Book del dominio """
        return Book(
            title=book_dto.title,
            author=book_dto.author,
            isbn=book_dto.isbn,
            published_date=book_dto.published_date,
            id = book_dto.id
        )

    @staticmethod
    def to_dto(book):
        """ Mapea Book del dominio a BookDTO """
        return BookDTO(
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            published_date=book.published_date
        )
