from django.conf.urls import include, url
from serial import views as serial_views

#from .views import SignUpView

urlpatterns = [
    url(r'^$', serial_views.list, name='serial_list'),
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)$', serial_views.detail, name='serial_detail'),
    url(r'^top/$', serial_views.top_rated, name='serial_top_rated'),
]
