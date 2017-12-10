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
    photo = models.ImageField(upload_to="photos/directors/", default="photos/none/default.png")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Writer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/writers/", default="photos/none/default.png")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/actors/", default="photos/none/default.png")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/creators/", default="photos/none/default.png")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Author)
    image = models.ImageField(upload_to="images/", default="images/none/blank_poster.jpg")

    def __str__(self):
        return f'{self.title}'


def tuplify(x):
    return (x, x)


current_year = datetime.now().year
YEARS = map(tuplify, range(1990, current_year + 1))


class Film(models.Model):
    title = models.CharField(max_length=60)
    year = models.IntegerField(choices=YEARS)
    image = models.ImageField(upload_to="images/films/", default="images/none/blank_poster.jpg")
    director = models.ForeignKey(Director, blank=True)
    writers = models.ManyToManyField(Writer, blank=True)
    actors = models.ManyToManyField(Actor, through='Filmcast', blank=True)
    category = models.ManyToManyField(Category, blank=True)
    description = models.CharField(max_length=200, default="""Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. Etiam maximus efficitur lacus, sit amet pretium lorem 
    iaculis id. Nulla hendrerit risus at justo imperdiet, eget sagittis felis consequat. 
    Ut tempor luctus felis id ullamcorper. Ut fringilla pharetra magna a scelerisque.
    Maecenas nec sem varius mi rhoncus scelerisque sed sed enim. Suspendisse
    blandit ante at ipsum feugiat, vitae ultrices enim blandit.""")

    def __str__(self):
        return f'{self.title}'


class Filmcast(models.Model):
    actor = models.ForeignKey(Actor)
    film = models.ForeignKey(Film)
    name = models.CharField(max_length=20)


current_year = datetime.now().year
YEARS = map(tuplify, range(1990, current_year + 1))


class Serial(models.Model):
    title = models.CharField(max_length=60)
    year = models.IntegerField(choices=YEARS)
    category = models.ManyToManyField(Category, blank=True)
    image = models.ImageField(upload_to="images/serials/", default="images/none/blank_poster.jpg")
    actors = models.ManyToManyField(Actor, through='Serialcast', blank=True)
    seasons = models.PositiveSmallIntegerField(default=1)
    creator = models.ManyToManyField(Creator, blank=True)
    description = models.CharField(max_length=200, default="""Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. Etiam maximus efficitur lacus, sit amet pretium lorem 
    iaculis id. Nulla hendrerit risus at justo imperdiet, eget sagittis felis consequat. 
    Ut tempor luctus felis id ullamcorper. Ut fringilla pharetra magna a scelerisque.
    Maecenas nec sem varius mi rhoncus scelerisque sed sed enim. Suspendisse
    blandit ante at ipsum feugiat, vitae ultrices enim blandit.""")

    def __str__(self):
        return f'{self.title}'


class Serialcast(models.Model):
    actor = models.ForeignKey(Actor)
    serial = models.ForeignKey(Serial)
    name = models.CharField(max_length=20)
