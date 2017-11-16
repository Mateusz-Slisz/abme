from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookSerializer, FilmSerializer, SerialSerializer
from .models import Author, Book, Film, Serial


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

class SerialViewSet(ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Serial.objects.all()
