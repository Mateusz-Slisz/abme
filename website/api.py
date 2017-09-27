from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, BookViewSet, FilmViewSet
 
 
router = DefaultRouter()
 
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('films', FilmViewSet)
 