from bookPlaylists.models import Books
from .models import Books

def addBook():
    name = str(input("Enter Book name: "))
    author = str(input("Enter Author: "))
    book = Books(book_name = name, book_author = author)
    book.save()

for i in range(5):
    addBook()