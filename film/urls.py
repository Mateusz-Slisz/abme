from django.conf.urls import url
from film import views as film_views


urlpatterns = [
    url(r'^$', film_views.list, name='film_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)$', film_views.detail, name='film_detail'),
    url(r'^top/$', film_views.top_rated, name='film_top_rated'),
]
