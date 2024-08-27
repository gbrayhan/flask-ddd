class Book:
    def __init__(self, title=None, author=None, isbn=None, published_date=None, id=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_date = published_date
        self.id = id

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'published_date': self.published_date.strftime("%Y-%m-%d") if self.published_date else None
        }

    def __repr__(self):
        return f"<Id {self.id}, Book {self.title}, Author: {self.author}, ISBN: {self.isbn}>"
