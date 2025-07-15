1. Open Django Shell
--------------------
Command:
>>> python manage.py shell

2. Import the Book Model
------------------------
Command:
>>> from bookshelf.models import Book

(Replace 'bookshelf' with the actual name of your app.)

3. Create a Book Instance
-------------------------
Command:
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Output:
<Book: 1984>