from api.models import Serial
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CHOICES = [(i, i) for i in range(11)]

class SerialRating(models.Model):
    user = models.ForeignKey(User)
    serial = models.ForeignKey(Serial)
    rate = models.IntegerField(choices=CHOICES, default=1)
    date = models.DateTimeField(default=timezone.now)


class SerialWatchlist(models.Model):
    user = models.ForeignKey(User)
    serial = models.ForeignKey(Serial)
    date = models.DateTimeField(default=timezone.now)
