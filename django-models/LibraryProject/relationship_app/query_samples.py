import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library

# Query all books by a specific author
author = Author.objects.get(name='John Doe')
books_by_author = Book.objects.filter(author=author)
print("Books by John Doe:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library = Library.objects.get(name='Central Library')
books_in_library = Book.objects.filter(library=library)
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian for {library.name}: {librarian.name}")
