from rest_framework.routers import DefaultRouter
from api.views import (
    PersonViewSet,
    CategoryViewSet, ArticleCategoryViewSet,
    FilmViewSet,
    SerialViewSet,
    FilmcastViewSet,
    SerialcastViewSet,
    ArticleViewSet,
    )


router = DefaultRouter()

router.register('Article Categories', ArticleCategoryViewSet)
router.register('Articles', ArticleViewSet)
router.register('Persons', PersonViewSet)
router.register('Categories', CategoryViewSet)
router.register('Films', FilmViewSet)
router.register('Serials', SerialViewSet)
router.register('Filmcasts', FilmcastViewSet)
router.register('Serialcasts', SerialcastViewSet)
