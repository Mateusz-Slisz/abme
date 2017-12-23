from rest_framework.serializers import ModelSerializer
from .models import Author, Person, Category, Book, Film, Serial, Filmcast, Serialcast


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'birthdate', 'biography', 'photo')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'image')


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year', 'directors', 'writers', 'actors', 'category', 'description', 'image')


class FilmcastSerializer(ModelSerializer):
    class Meta:
        model = Filmcast
        fields = ('id', 'actor', 'film', 'name')


class SerialSerializer(ModelSerializer):
    class Meta:
        model = Serial
        fields = ('id', 'title', 'year', 'seasons', 'creators', 'actors', 'category', 'description', 'image')


class SerialcastSerializer(ModelSerializer):
    class Meta:
        model = Serialcast
        fields = ('id', 'actor', 'serial', 'name')
