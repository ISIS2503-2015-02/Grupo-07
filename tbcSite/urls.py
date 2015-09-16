"""tbcSite URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pruebas.views import *
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from tbcSite import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cache/$', CacheView.as_view()),
    url(r'^cache/(?P<ide>[0-9]+)/$', CacheView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^tbcSite/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tbcSite/$', views.usuario_list),
    url(r'^tbcSite/$', views.reservasMobiBus_list),
    url(r'^tbcSite/$', views.conductoresTranvia_list),
    url(r'^tbcSite/$', views.tranvias_list),
    url(r'^tbcSite/$', views.lineas_list),
    url(r'^tbcSite/$', views.alertasTranvia_list),
    url(r'^tbcSite/$', views.coordenadasTranvia_list),
    url(r'^tbcSite/$', views.conductoresMoviBus_list),
    url(r'^tbcSite/$', views.moviBuses_list),
    url(r'^tbcSite/$', views.coordenadasMoviBus_list),
    url(r'^tbcSite/$', views.estacionesVcubs_list),
    url(r'^tbcSite/$', views.vcubs_list),
    url(r'^tbcSite/$', views.reportesMoviBus_list),
    url(r'^tbcSite/$', views.reportesTranvia_list),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.usuario_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.reservaMobiBus_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.conductorTranvia_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.tranvia_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.linea_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.alertaTranvia_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.coordenadasTranvia_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.conductorMoviBus_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.moviBus_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.coordenadasTranvia_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.estacionesVcubs_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.vcubs_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.reportesMoviBus_detail),
    url(r'^tbcSite/(?P<pk>[0-9]+)/$', views.reportesTranvia_detail),
]

urlpatterns += staticfiles_urlpatterns()
