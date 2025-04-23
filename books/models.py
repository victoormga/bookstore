from django.db import models
from django.conf import settings
from authors.models import Author

GENRE_CHOICES = [
    ('ficcion', 'Ficción'),
    ('fantasia', 'Fantasía'),
    ('scifi', 'Ciencia Ficción'),
    ('misterio', 'Misterio'),
]

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateField()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
