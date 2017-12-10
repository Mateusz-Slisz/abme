from rest_framework.viewsets import ModelViewSet
from .serializers import (
    AuthorSerializer, DirectorSerializer, WriterSerializer, ActorSerializer, CreatorSerializer,
    CategorySerializer,
    BookSerializer,
    FilmSerializer,
    SerialSerializer,
    FilmcastSerializer,
    SerialcastSerializer,
    )
from .models import Author, Director, Writer, Actor, Category, Creator, Book, Film, Serial, Filmcast, Serialcast


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


class CreatorViewSet(ModelViewSet):
    serializer_class = CreatorSerializer
    queryset = Creator.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class FilmViewSet(ModelViewSet):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()


class FilmcastViewSet(ModelViewSet):
    serializer_class = FilmcastSerializer
    queryset = Filmcast.objects.all()


class SerialViewSet(ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Serial.objects.all()


class SerialcastViewSet(ModelViewSet):
    serializer_class = SerialcastSerializer
    queryset = Serialcast.objects.all()
