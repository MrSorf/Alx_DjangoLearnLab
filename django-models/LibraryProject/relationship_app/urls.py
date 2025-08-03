from django.contrib import admin
from django.urls import path
from . import views
from views import BookListView
from views import list_books
from .views import list_books, LibraryDetailView
from .views import LoginView, LogoutView
urlpatterns = [
    path('books/', list_books, BookListView.as_view(), name='book_list'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    path('register/', views.register, name='reister'),
    
]
