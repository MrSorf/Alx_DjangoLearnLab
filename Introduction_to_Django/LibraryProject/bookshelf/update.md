 Update a Book Instance
-------------------------
Command:
>>> book = Book.objects.get(title="Nineteen Eighty Four")
>>> book.save()

Output:
(Book instance updated in the database)
