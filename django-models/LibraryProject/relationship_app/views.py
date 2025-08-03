from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import admin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "/relationship_app/register.html", {"form": form})

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")
