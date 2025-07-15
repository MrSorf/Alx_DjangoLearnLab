from django.contrib import admin

from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # add any options you like
    search_fields = ("title", "author")

admin.site.register(Book, BookAdmin)

