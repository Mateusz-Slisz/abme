from django.conf.urls import url
from person import views as person_views


urlpatterns = [
    url(r'^(?P<pk>\d+)/(?P<slug>[-\w]+)$',
        person_views.detail, name='person_detail'),
]
