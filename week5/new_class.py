# Base class: Book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

# Subclass: EBook
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    def get_description(self):
        return f"{super().get_description()} File size: {self.file_size}MB."

# Example usage
book = Book("1984", "George Orwell", 328)
print(book.get_description())

ebook = EBook("1984", "George Orwell", 328, 2.5)
print(ebook.get_description())