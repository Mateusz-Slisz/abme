"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views as main_views
from django.contrib.auth import views as auth_views
from .api import router
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home, name='website_home'),
    url(r'^login/$', auth_views.login, name='website_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'website_home'}, name='website_logout'),
    url(r'^api/', include(router.urls)),
    url(r'^user/', include('user.urls')),
    url(r'^films/', include('films.urls')),
    url(r'^books/', include('books.urls')),
    url(r'^serials/', include('serials.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^person/', include('person.urls')),
    url(r'^article/', include('article.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
