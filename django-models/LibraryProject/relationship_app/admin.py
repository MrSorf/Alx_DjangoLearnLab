from django.contrib import admin

from django.contrib.auth.models import Group

admin_group, created = Group.objects.get_or_create(name='Admin')
