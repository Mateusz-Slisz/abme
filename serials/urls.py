from django.conf.urls import include, url
from serials import views as serials_views

#from .views import SignUpView

urlpatterns = [
    url(r'^', serials_views.list, name='serial_list'),
]