from django.conf.urls import include, url
from search import views as search_views


urlpatterns = [
    url(r'^$', search_views.list, name='search_list'),
    url(r'^films/$', search_views.film_list, name='search_film_list'),
    url(r'^serials/$', search_views.serial_list, name='search_serial_list'),
]
