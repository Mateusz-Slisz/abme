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
    url(r'^film/', include('film.urls')),
    url(r'^serial/', include('serial.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^person/', include('person.urls')),
    url(r'^article/', include('article.urls')),
    url(r'^analytics/', include('analytics.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
