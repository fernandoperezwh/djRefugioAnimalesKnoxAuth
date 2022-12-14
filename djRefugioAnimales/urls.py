# coding=utf-8
"""djRefugioAnimales URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# django packages
from django.conf.urls import include, url
from django.contrib import admin
# local packages
from django.views.generic import TemplateView

from apps.api.views import home, ObtainAuthToken, VerifyAuthToken

urlpatterns = [
    # region django urls
    url(r'^admin/', include(admin.site.urls)),
    # endregion
    # region django rest framework urls
    url(r'api/auth/', include('knox.urls')),
    # endregion

    # region local urls
    url(r'^$', home, name='home'),
    url(r'^a/', include('apps.adopcion.urls')),
    url(r'^m/', include('apps.mascota.urls')),
    url(r'^api/', include('apps.api.urls'))
    # endregion
]
from django.views.static import serve 
from djRefugioAnimales import settings
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
