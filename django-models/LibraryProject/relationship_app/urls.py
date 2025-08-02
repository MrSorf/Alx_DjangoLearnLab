from django.contrib import admin
from django.urls import path
from views import BookListView
from views import list_books
from .views import list_books, LibraryDetailView
from .views import LoginView, LogoutView, RegisterView 
urlpatterns = [
    path('books/', list_books, BookListView.as_view(), name='book_list'),
    path('login/', LoginView.as_view(name='relationship_app/login.html')),
    path('logout/', LogoutView.as_view(name='relationship_app/login.html')),
    path('register/', RegisterView(name='relationship_app/login.html')),
    
]
