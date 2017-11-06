from django.db import models
from api.models import Book
from django.contrib.auth.models import User

CHOICES = [(i, i) for i in range(11)]

class BookRating(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    rate = models.IntegerField(choices=CHOICES, default=1)
