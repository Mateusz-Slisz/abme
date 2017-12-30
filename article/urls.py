from django.conf.urls import url
from article import views as article_views


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', article_views.detail, name='article_detail'),
]
