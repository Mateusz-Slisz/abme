from rest_framework.viewsets import ModelViewSet
from .serializers import (
    AuthorSerializer, PersonSerializer,
    CategorySerializer,
    BookSerializer,
    FilmSerializer,
    SerialSerializer,
    FilmcastSerializer,
    SerialcastSerializer,
    )
from .models import Author, Person, Category, Book, Film, Serial, Filmcast, Serialcast


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


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
