class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def describe(self):
        return f"'{self.title}' by {self.author} ({self.genre})"
    
class EBook(Book):
    def __init__(self, title, author, genre, file_format):
        super().__init__(title, author, genre)
        self.file_format = file_format

    def describe(self):
        return f"'{self.title}' by {self.author} ({self.genre}), File format: {self.file_format}"
    
book1 = Book("Fiica padurarului", "J.Colins", "horror")
print(book1.describe())
ebook1 = EBook("We all die in the end", "T.Roberts", "Romance", "pdf")
print(ebook1.describe())