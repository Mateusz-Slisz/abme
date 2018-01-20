from django.conf.urls import url
from person import views as person_views


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)-(?P<pk>\d+)/$',
        person_views.detail, name='person_detail'),
]
