from rest_framework.routers import DefaultRouter
from api.views import (
    AuthorViewSet, PersonViewSet,
    CategoryViewSet,
    BookViewSet,
    FilmViewSet,
    SerialViewSet,
    FilmcastViewSet,
    SerialcastViewSet,
    )


router = DefaultRouter()


router.register('authors', AuthorViewSet)
router.register('persons', PersonViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('films', FilmViewSet)
router.register('serials', SerialViewSet)
router.register('filmcast', FilmcastViewSet)
router.register('serialcast', SerialcastViewSet)
