from django.conf.urls import url
from person import views as person_views


urlpatterns = [
    url(r'^(?P<first_name>[\w.@+-]+)-(?P<last_name>[\w.@+-]+)$',
        person_views.detail, name='person_detail'),
]
