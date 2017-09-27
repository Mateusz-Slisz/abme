from django.db import models
from datetime import datetime
 
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
 
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
 
 
class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Author)
 
    def __str__(self):
        return f'{self.title}'


def tuplify(x): 
    return (x,x)


current_year = datetime.now().year
YEARS = map(tuplify, range(1990, current_year + 1)) 


class Film(models.Model):
    title = models.CharField(max_length=60)
    year = models.IntegerField(choices=YEARS)
