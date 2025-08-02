from django.shortcuts import render
from django.views.generic import ListView
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

class BookListView(ListView):
    model = Library 
    template_name = "relationship_app/library_detail.html"


class LibraryDetailView(DetailView):
    model = Library 
    template_name = "relationship_app/library_detail.html"

class LoginView(login):
      template_name = 'relationship_app/login.html'

class LogoutView(logout):
     template_name = 'relationship_app/logout.html'

class RegisterView(FormView):
     template_name = 'relationship_app/register.html'
     form_class = UserCreationForm
     success_url = reverse_lazy('login')

def form_valid(self, form):
        form.save()
        return super().form_valid(form)