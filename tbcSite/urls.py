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
    # url(r'^cache/$', CacheView.as_view()),
    # url(r'^cache/(?P<ide>[0-9]+)/$', CacheView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^tbcSite/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^usuarios/$', views.UsuarioList.as_view()),
    #url(r'^reservasUsuarios/$', views.ReservaMobiBusList.as_view()),
    #url(r'^conductoresTranvia/$', views.ConductorTranviaList.as_view()),
    url(r'^tranvias/$', views.TranviaList.as_view()),
    url(r'^lineas/$', views.LineaList.as_view()),
    #url(r'^alertas/$', views.AlertaTranviaList.as_view()),
    #url(r'^coordenadasTranvia/$', views.CoordenadasTranviaList.as_view()),
    #url(r'^conductoresMobiBus/$', views.ConductorMoviBusList.as_view()),
    url(r'^movibuses/$', views.MoviBusList.as_view()),
    #url(r'^coordenadasMovibus/$', views.CoordenadasMoviBusList.as_view()),
    url(r'^estaciones/$', views.EstacionVcubsList.as_view()),
    url(r'^vcubs/$', views.VcubsList.as_view()),
    #url(r'^reportesMovibuses/$', views.ReporteMoviBusList.as_view()),
    #url(r'^reportesTranvias/$', views.ReporteTranviaList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
    #url(r'^reservasUsuarios/(?P<pk>[0-9]+)/$', views.ReservaMobiBusDetail.as_view()),
    #url(r'^conductoresTranvia/(?P<pk>[0-9]+)/$', views.ConductorTranviaDetail.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/$', views.TranviaDetail.as_view()),
    url(r'^lineas/(?P<pk>[0-9]+)/$', views.LineaDetail.as_view()),
    #url(r'^alertas/(?P<pk>[0-9]+)/$', views.AlertaTranviaDetail.as_view()),
    #url(r'^coordenadasTranvia/(?P<pk>[0-9]+)/$', views.ConductorTranviaDetail.as_view()),
    #url(r'^conductoresMoviBus/(?P<pk>[0-9]+)/$', views.ConductorMoviBusDetail.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/$', views.MoviBusDetail.as_view()),
    #url(r'^coordenadasMovibus/(?P<pk>[0-9]+)/$', views.ConductorMoviBusDetail.as_view()),
    url(r'^estaciones/(?P<pk>[0-9]+)/$', views.EstacionVcubsDetail.as_view()),
    url(r'^vcubs/(?P<pk>[0-9]+)/$', views.VcubsDetail.as_view()),
    #url(r'^reportesMovibuses/(?P<pk>[0-9]+)/$', views.ReservaMobiBusDetail.as_view()),
    #url(r'^reportesTranvias/(?P<pk>[0-9]+)/$', views.ReporteTranviaDetail.as_view()),

    url(r'^usuarios/(?P<pk>[0-9]+)/reservas/$', views.ReservaMobiBusList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/reservas/(?P<pk1>[0-9]+)/$', views.ReservaMobiBusDetail.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/conductores/$', views.ConductorTranviaList.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/conductores/(?P<pk1>[0-9]+)$', views.ConductorTranviaDetail.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/coordenadas/$', views.CoordenadasTranviaList.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/coordenadas/(?P<pk1>[0-9]+)/$', views.CoordenadasTranviaDetail.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/alertas/$', views.AlertaTranviaList.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/alertas/(?P<pk1>[0-9]+)/$', views.AlertaTranviaDetail.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/reportes/$', views.ReporteTranviaList.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/reportes/(?P<pk1>[0-9]+)/$', views.ReporteTranviaDetail.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/conductores/$', views.ConductorMoviBusList.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/conductores/(?P<pk1>[0-9]+)/$', views.ConductorMoviBusDetail.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/coordenadas/$', views.CoordenadasMoviBusList.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/coordenadas/(?P<pk1>[0-9]+)/$', views.CoordenadasMoviBusDetail.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/reportes/$', views.ReporteMoviBusList.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/reportes/(?P<pk1>[0-9]+)/$', views.ReporteMoviBusDetail.as_view()),
    url(r'^estaciones/(?P<pk>[0-9]+)/vcubs/$', views.VcubsList.as_view()),
    url(r'^estaciones/(?P<pk>[0-9]+)/vcubs/(?P<pk1>[0-9]+)/$', views.VcubsDetail.as_view()),





]

urlpatterns += staticfiles_urlpatterns()
