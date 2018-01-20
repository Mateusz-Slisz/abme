from django.conf.urls import url
from article import views as article_views


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)-(?P<pk>\d+)$', article_views.detail, name='article_detail'),
    url(r'^category/(?P<name>[\w ]+)$', article_views.category, name='article_category')
]
