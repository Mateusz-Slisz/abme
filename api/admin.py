from django.contrib import admin
from .models import Person, Category, Film, Serial, Filmcast, Serialcast, ArticleCategory, Article


class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'first_name', 'last_name', 'birthdate')
    list_display_links = ('__str__', 'first_name', 'last_name', 'birthdate')
    list_filter = ('birthdate',)
    search_fields = ('first_name', 'last_name', 'birthdate')
    class Meta:
        model = Person


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    class Meta:
        model = Category


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'get_directors', 'get_writers', 'get_categories')
    list_display_links = ('title', 'year', 'get_directors', 'get_writers', 'get_categories')
    list_filter = ('directors', 'writers', 'actors', 'category', 'year')
    search_fields = ('title', 'year', 'category__name',
                     'directors__first_name', 'directors__last_name',
                     'writers__first_name', 'writers__last_name',
                     'actors__first_name', 'actors__last_name',)
    class Meta:
        model = Film

    def get_directors(self, film):
        return "\n".join(str(i) for i in film.directors.all())

    def get_writers(self, film):
        return "\n".join(str(i) for i in film.writers.all())

    def get_categories(self, film):
        return "\n".join(i.name for i in film.category.all())


class SerialAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'seasons', 'get_creators', 'get_categories')
    list_display_links = ('title', 'year', 'seasons', 'get_creators', 'get_categories')
    list_filter = ('creators', 'category', 'seasons', 'year')
    search_fields = ('title', 'year', 'category__name', 'seasons',
                     'creators__first_name', 'creators__last_name',
                     'actors__first_name', 'actors__last_name',)
    class Meta:
        model = Serial

    def get_creators(self, serial):
        return "\n".join(str(i) for i in serial.creators.all())

    def get_categories(self, serial):
        return "\n".join(i.name for i in serial.category.all())


class FilmcastAdmin(admin.ModelAdmin):
    list_display = ('actor', 'film', 'name')
    list_display_links = ('actor', 'film', 'name')
    search_fields = ('actor__first_name', 'actor__last_name', 'film__title', 'name')
    class Meta:
        model = Filmcast


class SerialcastAdmin(admin.ModelAdmin):
    list_display = ('actor', 'serial', 'name')
    list_display_links = ('actor', 'serial', 'name')
    search_fields = ('actor__first_name', 'actor__last_name', 'serial__title', 'name')
    class Meta:
        model = Serialcast


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    class Meta:
        model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'get_categories',)
    list_display_links = ('title', 'created_date', 'get_categories')
    list_filter = ('created_date', 'category')
    search_fields = ('title', 'text', 'created_date', 'category__name')
    class Meta:
        model = Article

    def get_categories(self, article):
        return "\n".join(i.name for i in article.category.all())


admin.site.register(Category, CategoryAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Serialcast, SerialcastAdmin)
admin.site.register(Filmcast, FilmcastAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Serial, SerialAdmin)
admin.site.register(Article, ArticleAdmin)
