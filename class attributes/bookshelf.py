class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
class BookContainer:
    def __init__(self):
        self.books = []
    def add_book(self, book: Book):
        self.books.append(book)
    def list_books(self):
        for book in self.books:
            print(f"{book.name} ({book.author})")
class Bookshelf(BookContainer):
    def __init__(self):
        super().__init__()
    def add_book(self, book: Book, location: int):
        self.books.insert(location, book)
if __name__ == "__main__":
   # Create some books for testing
   b1 = Book("Old Man and the Sea", "Ernest Hemingway")
   b2 = Book("Silent Spring", "Rachel Carson")
   b3 = Book("Pride and Prejudice", "Jane Austen")

   # Create a BookContainer and add the books
   container = BookContainer()
   container.add_book(b1)
   container.add_book(b2)
   container.add_book(b3)

   # Create a Bookshelf and add the books (always to the beginning)
   shelf = Bookshelf()
   shelf.add_book(b1, 0)
   shelf.add_book(b2, 0)
   shelf.add_book(b3, 0)


   # Tulostetaan
   print("Container:")
   container.list_books()

   print()

   print("Shelf:")
   shelf.list_books()