from rest_framework.routers import DefaultRouter
from api.views import (
    AuthorViewSet, DirectorViewSet, WriterViewSet, ActorViewSet, CreatorViewSet,
    CategoryViewSet,
    BookViewSet,
    FilmViewSet,
    SerialViewSet,
    FilmcastViewSet,
    SerialcastViewSet,
    )


router = DefaultRouter()


router.register('authors', AuthorViewSet)
router.register('directors', DirectorViewSet)
router.register('writers', WriterViewSet)
router.register('actors', ActorViewSet)
router.register('creators', CreatorViewSet)
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('films', FilmViewSet)
router.register('serials', SerialViewSet)
router.register('filmcast', FilmcastViewSet)
router.register('serialcast', SerialcastViewSet)
