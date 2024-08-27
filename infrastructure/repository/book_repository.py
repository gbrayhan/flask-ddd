from infrastructure.database import db
from infrastructure.repository.models import BookDTO
from infrastructure.repository.book_mapper import BookMapper

class BookRepository:
    def add(self, book):
        book_dto = BookMapper.to_dto(book)
        try:
            db.session.add(book_dto)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    def remove(self, book_id):
        try:
            book_dto = BookDTO.query.get(book_id)
            if book_dto:
                db.session.delete(book_dto)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False

    def update(self, book_id, data):
        try:
            book_dto = BookDTO.query.get(book_id)
            if book_dto:
                for key, value in data.items():
                    setattr(book_dto, key, value)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False

    def get(self, book_id):
        try:
            book_dto = BookDTO.query.get(book_id)
            if book_dto:
                return BookMapper.to_domain(book_dto)
            return None
        except Exception as e:
            return None

    def list_all(self):
        try:
            book_dtos = BookDTO.query.all()
            return [BookMapper.to_domain(book_dto) for book_dto in book_dtos]
        except Exception as e:
            return []
