from django.contrib import admin
from django.urls import path
from views import BookListView
from views import list_books
from .views import list_books, LibraryDetailView
urlpatterns = [
    path('books/', list_books, BookListView.as_view(), name='book_list'),
    path('login/', LoginView.as_view(name='login.html'))
    path('logout/', LogoutView.as_view(name='logout.html'))
    path('register/', views.register(name='register.html'))
    
]
