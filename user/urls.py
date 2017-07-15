from django.conf.urls import include, url
from user import views as user_views

#from .views import SignUpView

urlpatterns = [
    url(r'^home$', user_views.home, name='user_home'),
]

