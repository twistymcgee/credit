from django.contrib import admin

from .models import Account, Category, Person

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Person)
