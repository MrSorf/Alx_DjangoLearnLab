1.  Retrieve a Book Instance
    ---------------------------
    Command:
    >>> book = Book.objects.get(title="1984")
    
    Output:
    1984

2.  Retrieve All Books
    ---------------------
    Command:
    >>> books = Book.objects.all()
    
    Output:
    1984
    

3.  Filter Books by Author
    -------------------------
    Command:
    >>> books = Book.objects.filter(author="George Orwell")

    Output:
    1984