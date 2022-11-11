class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book1 = Book("Book1")
book2 = Book("Book2")
shelf = BookShelf(book1, book2)

print(shelf)
            
