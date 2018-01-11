from rest_framework.serializers import ModelSerializer
from .models import Person, Category, Film, Serial, Filmcast, Serialcast, ArticleCategory, Article


class ArticleCategorySerializer(ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ('id', 'name')


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'image', 'category', 'created_date')


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'birthdate', 'biography', 'photo')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


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
