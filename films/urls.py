from django.conf.urls import include, url
from films import views as films_views

#from .views import SignUpView

urlpatterns = [
    url(r'^', films_views.list, name='film_list'),
]