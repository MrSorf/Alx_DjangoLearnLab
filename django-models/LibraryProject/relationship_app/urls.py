
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from views import BookListView
from views import list_books
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, BookListView.as_view(), name='book_list'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),
     path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book_view, name='delete_book'),
]