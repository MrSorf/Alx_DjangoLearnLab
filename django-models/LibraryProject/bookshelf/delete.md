Delete a Single Book
-----------------------

from bookshelf.models import Book

Command:
>>> book = Book.objects.get(title="Nineteen Eighty Four")
>>> book.delete()

Output:
(1, {'bookshelf.Book': 1})

9. Delete All Books with Title "Nineteen Eighty Four"
-------------------------------------
Command:
>>> Book.objects.filter(title="Nineteen Eighty Four").delete()

Output:
(2, {'bookshelf.Book': 2})

10. Check if a Book Exists
--------------------------
Command:
>>> Book.objects.filter(title="Nineteen Eighty Four").exists()

Output:
True / False
`