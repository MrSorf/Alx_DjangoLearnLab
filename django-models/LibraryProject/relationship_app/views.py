from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

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

#class LoginView(login):
      #template_name = 'relationship_app/login.html'

#lass LogoutView(logout):
     #template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def is_admin(user):
     return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member(request):
   return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    pass 

@permission_required('relationship_app.can_delete_book')
def delete_book_view(request, pk):
    # your delete logic here
    pass

@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    # your add logic here
    pass