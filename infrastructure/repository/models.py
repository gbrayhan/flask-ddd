# infrastructure/repository/models.py

from sqlalchemy import Column, Integer, String, Date
from infrastructure.database import db

class BookDTO(db.Model):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    isbn = Column(String(20), nullable=False)
    published_date = Column(Date)

    def __repr__(self):
        return f"<BookDTO(title={self.title}, author={self.author}, isbn={self.isbn})>"
