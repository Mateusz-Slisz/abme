from rest_framework.serializers import ModelSerializer
from .models import Author, Book, Film, Serial
 
 
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')
 
 
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'title', 'image')


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year', 'image')


class SerialSerializer(ModelSerializer):
    class Meta:
        model = Serial
        fields = ('id', 'title', 'seasons', 'image')
        
