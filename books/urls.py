from django.conf.urls import include, url
from books import views as books_views

#from .views import SignUpView

urlpatterns = [
    url(r'^', books_views.list, name='book_list'),
]