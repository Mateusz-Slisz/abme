from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, DirectorSerializer, WriterSerializer, BookSerializer, FilmSerializer, SerialSerializer
from .models import Author, Director, Writer, Book, Film, Serial


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class WriterViewSet(ModelViewSet):
    serializer_class = WriterSerializer
    queryset = Writer.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()


class SerialViewSet(ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Serial.objects.all()
