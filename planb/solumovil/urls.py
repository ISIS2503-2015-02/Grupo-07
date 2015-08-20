"""solumovil URL Configuration

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

from transport.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Transport urls
    url(r'^transport/$', TransportView.as_view(), name='transport_all'),
    url(r'^transport/(?P<pk>[0-9]+)/$', TransportView.as_view(), name='transport_pk'),

    # Historic urls
    url(r'^historic/$', HistoricView.as_view(), name='historic_all'),
    url(r'^historic/(?P<transport_pk>[0-9]+)/$', HistoricView.as_view(), name='historic_pk')
]
