from django.shortcuts import render
from django.views.generic import ListView
from .models import Library
from .models import Book
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books}, content_type='text/plain')

class BookListView(ListView):
    model = Library 
    template_name = "book_list.txt"


