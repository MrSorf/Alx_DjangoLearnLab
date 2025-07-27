from django.shortcuts import render
from django.views.generic import ListView
from .models import Library
# Create your views here.
def list_books(request):
    return render(request, 'book_list.txt', content_type='text/plain')

class BookListView(ListView):
    model = Library 
    template_name = "book_list.txt"


