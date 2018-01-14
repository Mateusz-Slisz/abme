from django.conf.urls import url
from analytics import views as analytics_views


urlpatterns = [
    url(r'^$', analytics_views.main, name='analytics'),
]
