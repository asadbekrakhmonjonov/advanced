class Book():
    def __init__(self, title, author,genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
def older_book(book1: Book, book2: Book):
    if book1.year < book2.year:
        print(f"{book1.title} is older. It was published in {book1.year}")
    elif book2.year < book1.year:
        print(f"{book2.title} is older.It was published in {book2.year}")
    elif book1.year == book2.year:
        print(f"{book1.title} and {book2.title} were published in {book1.year}")
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)
