from django.conf.urls import include, url
from user import views as user_views

#from .views import SignUpView

urlpatterns = [
    url(r'^home', user_views.home, name='user_home'),
    url(r'^signup', user_views.signup, name='user_signup'),
    url(r'^settings$', user_views.settings, name='user_settings'),
    url(r'^watchlist$', user_views.watchlist, name='user_watchlist'),
    url(r'^(?P<username>[\w.@+-]+)$', user_views.profile, name='user_profile'),
    url(r'^(?P<username>[\w.@+-]+)/films$', user_views.profile_films, name='user_profile_films'),
    url(r'^(?P<username>[\w.@+-]+)/books$', user_views.profile_books, name='user_profile_books'),
    url(r'^(?P<username>[\w.@+-]+)/serials$', user_views.profile_serials, name='user_profile_serials'),
]
