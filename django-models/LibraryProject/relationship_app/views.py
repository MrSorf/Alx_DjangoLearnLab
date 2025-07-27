from django.shortcuts import render
from django.views.generic import ListView
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

class BookListView(ListView):
    model = Library 
    template_name = "relationship_app/library_detail.html"


