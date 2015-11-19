"""taxis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password_reset_recover/', include('password_reset.urls')),
    url(r'^$', 'taxi.views.index', name='index'),
    url(r'^know_more/(?P<id>\d+)/$', 'taxi.views.know_more', name='know_more'),
    url(r'^contacts/$', 'taxi.views.contacts', name='contacts'),
    url(r'registeration_taxi/$', 'taxi.views.registeration_taxi', name='registeration_taxi'),
    url(r'registration_user/$', 'taxi.views.registration_user', name='registration_user'),
    url(r'taxi_login/$', 'taxi.views.taxi_login', name='taxi_login'),
    url(r'user_logout/$', 'taxi.views.user_logout', name='user_logout'),
    url(r'personal_account/$', 'taxi.views.personal_account', name='personal_account'),
    url(r'personal_account/(?P<id>\d+)/$', 'taxi.views.delete', name='delete'),
    url(r'password_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'change_password.html'}, name='password_change'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

