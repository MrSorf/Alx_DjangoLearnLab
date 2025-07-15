
LibraryProject/bookshelf/create.md /

Django Shell CRUD Operations for Book Model
===========================================

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

4. Retrieve a Book Instance
---------------------------
Command:
>>> book = Book.objects.get(title="1984")


Output:
1984

5. Retrieve All Books
---------------------
Command:
>>> books = Book.objects.all()


Output:
1984
1984
...

6. Filter Books by Author
-------------------------
Command:
>>> books = Book.objects.filter(author="George Orwell")


Output:
1984
...

7. Update a Book Instance
-------------------------
Command:
>>> book = Book.objects.get(title="Nineteen Eighty Four")
>>> book.save()

Output:
(Book instance updated in the database)

8. Delete a Single Book
-----------------------
Command:
>>> book = Book.objects.get(title="1984")
>>> book.delete()

Output:
(1, {'bookshelf.Book': 1})

9. Delete All Books with Title "1984"
-------------------------------------
Command:
>>> Book.objects.filter(title="1984").delete()

Output:
(2, {'bookshelf.Book': 2})

10. Check if a Book Exists
--------------------------
Command:
>>> Book.objects.filter(title="1984").exists()

Output:
True / False

