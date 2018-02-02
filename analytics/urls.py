from django.conf.urls import url
from analytics import views as analytics_views


urlpatterns = [
    url(r'^$', analytics_views.main, name='analytics'),
    url(r'^month/$', analytics_views.month, name='analytics_month')
]
