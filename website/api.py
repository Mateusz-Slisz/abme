from rest_framework.routers import DefaultRouter
from api.views import (
    AuthorViewSet, DirectorViewSet, WriterViewSet, ActorViewSet,
    CategoryViewSet,
    BookViewSet,
    FilmViewSet,
    SerialViewSet,
    )


router = DefaultRouter()


router.register('authors', AuthorViewSet)
router.register('directors', DirectorViewSet)
router.register('writers', WriterViewSet)
router.register('actors', ActorViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('films', FilmViewSet)
router.register('serials', SerialViewSet)
