from django.contrib import admin

from .models import Author, Book, BookType

admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Author)
