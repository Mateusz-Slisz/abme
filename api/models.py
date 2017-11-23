from django.db import models
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Director(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Writer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Author)
    image = models.ImageField(upload_to="images/", default="images/none/blank_poster.jpg")

    def __str__(self):
        return f'{self.title}'


def tuplify(x):
    return (x,x)


current_year = datetime.now().year
YEARS = map(tuplify, range(1990, current_year + 1)) 


class Film(models.Model):
    title = models.CharField(max_length=60)
    year = models.IntegerField(choices=YEARS)
    image = models.ImageField(upload_to="images/", default="images/none/blank_poster.jpg")
    director = models.ForeignKey(Director)
    writers = models.ManyToManyField(Writer)
    description = models.CharField(max_length=200, default="""Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. Etiam maximus efficitur lacus, sit amet pretium lorem 
    iaculis id. Nulla hendrerit risus at justo imperdiet, eget sagittis felis consequat. 
    Ut tempor luctus felis id ullamcorper. Ut fringilla pharetra magna a scelerisque.
    Maecenas nec sem varius mi rhoncus scelerisque sed sed enim. Suspendisse
    blandit ante at ipsum feugiat, vitae ultrices enim blandit.""")

    def __str__(self):
        return self.title


class Serial(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to="images/", default="images/none/blank_poster.jpg")
    seasons = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title
