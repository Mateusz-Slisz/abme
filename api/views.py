from rest_framework.viewsets import ModelViewSet
from .serializers import (
    AuthorSerializer, DirectorSerializer, WriterSerializer, ActorSerializer,
    CategorySerializer,
    BookSerializer,
    FilmSerializer,
    SerialSerializer,
    )
from .models import Author, Director, Writer, Actor, Category, Book, Film, Serial


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class WriterViewSet(ModelViewSet):
    serializer_class = WriterSerializer
    queryset = Writer.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()


class SerialViewSet(ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Serial.objects.all()
