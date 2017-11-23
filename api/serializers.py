from rest_framework.serializers import ModelSerializer
from .models import Author, Director, Writer, Book, Film, Serial


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'first_name', 'last_name')


class WriterSerializer(ModelSerializer):
    class Meta:
        model = Writer
        fields = ('id', 'first_name', 'last_name')


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'image')


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year', 'director', 'writers', 'description', 'image')


class SerialSerializer(ModelSerializer):
    class Meta:
        model = Serial
        fields = ('id', 'title', 'seasons', 'image')
