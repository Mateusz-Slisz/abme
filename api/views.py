from rest_framework.viewsets import ModelViewSet
from .serializers import (
    PersonSerializer,
    CategorySerializer, ArticleCategorySerializer,
    FilmSerializer,
    SerialSerializer,
    FilmcastSerializer,
    SerialcastSerializer,
    ArticleSerializer,
    )
from .models import Person, Category, Film, Serial, Filmcast, Serialcast, ArticleCategory, Article


class ArticleCategoryViewSet(ModelViewSet):
    serializer_class = ArticleCategorySerializer
    queryset = ArticleCategory.objects.all()


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


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
