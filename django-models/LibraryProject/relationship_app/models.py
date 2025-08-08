from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
class Author(models.Model):
    name = models.CharField(max_length=100)
def __str__(self):
    return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100, default='Default Library')
    books = models.ManyToManyField('Book')
def __str__(self):
    return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
def __str__(self):
    return self.name

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

def __str__(self):
 return f"{self.user.username} - {self.role}"