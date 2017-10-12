from django.conf.urls import include, url
from user import views as user_views

#from .views import SignUpView

urlpatterns = [
    url(r'^home', user_views.home, name='user_home'),
    url(r'^signup', user_views.signup, name='user_signup'),
    url(r'^settings$', user_views.settings, name='user_settings'),
    url(r'^settings/films$', user_views.settings_films, name='user_settings_film'),
    url(r'^settings/books$', user_views.settings_books, name='user_settings_books'),
    url(r'^(?P<username>[\w.@+-]+)$', user_views.profile, name='user_profile'),
]
