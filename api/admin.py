from django.contrib import admin
from .models import Person, Category, Film, Serial, Filmcast, Serialcast, ArticleCategory, Article


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthdate')
    list_display_links = ('first_name', 'last_name', 'birthdate')
    search_fields = ('first_name', 'last_name')
    class Meta:
        model = Person


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    class Meta:
        model = Category


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    class Meta:
        model = Film


class SerialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    class Meta:
        model = Serial


class FilmcastAdmin(admin.ModelAdmin):
    list_display = ('actor', 'film')
    list_display_links = ('actor', 'film')
    search_fields = ('actor', 'film')
    class Meta:
        model = Filmcast


class SerialcastAdmin(admin.ModelAdmin):
    list_display = ('actor', 'serial')
    list_display_links = ('actor', 'serial')
    search_fields = ('actor', 'serial')
    class Meta:
        model = Serialcast


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    class Meta:
        model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_date')
    list_display_links = ('title', 'text', 'created_date')
    search_fields = ('title', 'text', 'created_date', 'category')
    class Meta:
        model = Article

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Filmcast, FilmcastAdmin)
admin.site.register(Serial, SerialAdmin)
admin.site.register(Serialcast, SerialcastAdmin)
