from django.contrib import admin
from django.urls import path
from views import BookListView
from views import list_books
from .views import list_books, LibraryDetailView
from .views import UserloginView, UserlogoutView, RegisterView
urlpatterns = [
    path('books/', list_books, BookListView.as_view(), name='book_list'),
    path('login/', UserloginView.as_view(), name='login'),
    path('logout/', UserlogoutView.as_view(), name='logout')
    path('register/', RegisterView.as_view(), name='register'),
    
]
