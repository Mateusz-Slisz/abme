from api.models import Film
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CHOICES = [(i, i) for i in range(11)]

class FilmRating(models.Model):
    user = models.ForeignKey(User)
    film = models.ForeignKey(Film)
    rate = models.IntegerField(choices=CHOICES, default=1)
    date = models.DateTimeField(default=timezone.now)


class FilmWatchlist(models.Model):
    user = models.ForeignKey(User)
    film = models.ForeignKey(Film)
    date = models.DateTimeField(default=timezone.now)
