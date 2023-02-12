from django.db import models


class BookType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Book(models.Model):
    name = models.CharField("Name of book", max_length=255)
    description = models.TextField("Description of book")
    type_of_book = models.ManyToManyField(BookType)
    authors = models.ManyToManyField(Author)
