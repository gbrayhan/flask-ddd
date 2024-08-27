class Book:
    def __init__(self, title=None, author=None, isbn=None, published_date=None):
        """
        Inicializa una nueva instancia de la clase Book.

        :param id: ID único del libro (opcional).
        :param title: Título del libro.
        :param author: Autor del libro.
        :param isbn: ISBN del libro.
        :param published_date: Fecha de publicación del libro (opcional).
        """
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_date = published_date

    def __repr__(self):
        """
        Representación en cadena de la instancia de Book.

        :return: Una cadena que representa el libro.
        """
        return f"<Book {self.title}, ISBN {self.isbn}>"

