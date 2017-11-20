from django.conf.urls import include, url
from books import views as books_views

#from .views import SignUpView

urlpatterns = [
    url(r'^$', books_views.list, name='book_list'),
    url(r'^(?P<pk>[0-9]+)/$', books_views.detail, name='book_detail'),
]