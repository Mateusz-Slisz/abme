from django.conf.urls import include, url
from serials import views as serials_views

#from .views import SignUpView

urlpatterns = [
    url(r'^$', serials_views.list, name='serial_list'),
    url(r'^(?P<slug>[-\w]+)-(?P<pk>\d+)/$', serials_views.detail, name='serial_detail'),
    url(r'^top/$', serials_views.top_rated, name='serial_top_rated'),
]
