from rest_framework.routers import DefaultRouter
from api.views import (
    AuthorViewSet, PersonViewSet,
    CategoryViewSet, ArticleCategoryViewSet,
    BookViewSet,
    FilmViewSet,
    SerialViewSet,
    FilmcastViewSet,
    SerialcastViewSet,
    ArticleViewSet,
    )


router = DefaultRouter()

router.register('Article Categories', ArticleCategoryViewSet)
router.register('Articles', ArticleViewSet)
router.register('Authors', AuthorViewSet)
router.register('Persons', PersonViewSet)
router.register('Categories', CategoryViewSet)
router.register('Books', BookViewSet)
router.register('Films', FilmViewSet)
router.register('Serials', SerialViewSet)
router.register('Filmcasts', FilmcastViewSet)
router.register('Serialcasts', SerialcastViewSet)
