import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library

# Query all books by a specific author
author_name = 'John Doe'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = 'Central Library'
library = Library.objects.get(name=library_name)

books = library.book_set
books = books.all() 
print(f"\nBooks in {library_name}:")
for book in books:
    print(book.title)

# Retrieve the librarian for a library
from relationship_app.models import Librarian  # make sure this is at the top
librarian = Librarian.objects.get(library=library) 
print(f"\nLibrarian for {library.name}: {librarian.name}")
