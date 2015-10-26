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
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from movibuses.views import ConductorMoviBusList, ConductorMoviBusDetail, MoviBusList, MoviBusDetail, CoordenadasMoviBusList, CoordenadasMoviBusDetail, ReporteMoviBusList, ReporteMoviBusDetail, RecorridoMoviBusList, RecorridoMoviBusDetail
from tranvias.views import ConductorTranviaList, TranviaList, CoordenadasTranviaList, ReporteTranviaList, AlertaTranviaList, LineaList, ConductorTranviaDetail, TranviaDetail, CoordenadasTranviaDetail, ReporteTranviaDetail, AlertaTranviaDetail, LineaDetail, RecorridoTranviaList, RecorridoTranviaDetail
from usuarios.views import UsuarioList, ReservaMobiBusList, UsuarioDetail, ReservaMobiBusDetail
from vcubs.views import EstacionVcubsList, EstacionVcubsDetail, VcubsList, VcubsDetail
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from auth.views import Auth

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'auth/$', Auth.as_view()),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^cache/$', CacheView.as_view()),
    # url(r'^cache/(?P<ide>[0-9]+)/$', CacheView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^tbcSite/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^usuarios/$', UsuarioList.as_view()),
    url(r'^reservasUsuario/$', ReservaMobiBusList.as_view()),
    url(r'^conductoresTranvia/$', ConductorTranviaList.as_view()),
    url(r'^tranvias/$', TranviaList.as_view()),
    url(r'^lineas/$', LineaList.as_view()),
    url(r'^alertas/$', AlertaTranviaList.as_view()),
    url(r'^coordenadasTranvia/$', CoordenadasTranviaList.as_view()),
    url(r'^conductoresMovibus/$', ConductorMoviBusList.as_view()),
    url(r'^movibuses/$', MoviBusList.as_view()),
    url(r'^coordenadasMovibus/$', CoordenadasMoviBusList.as_view()),
    url(r'^estaciones/$', EstacionVcubsList.as_view()),
    url(r'^vcubs/$', VcubsList.as_view()),
    url(r'^reportesMovibus/$', ReporteMoviBusList.as_view()),
    url(r'^reportesTranvia/$', ReporteTranviaList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', UsuarioDetail.as_view()),
    url(r'^reservasUsuario/(?P<pk>[0-9]+)/$', ReservaMobiBusDetail.as_view()),
    url(r'^conductoresTranvia/(?P<pk>[0-9]+)/$', ConductorTranviaDetail.as_view()),
    url(r'^tranvias/(?P<pk>[0-9]+)/$', TranviaDetail.as_view()),
    url(r'^lineas/(?P<pk>[0-9]+)/$', LineaDetail.as_view()),
    url(r'^alertas/(?P<pk>[0-9]+)/$', AlertaTranviaDetail.as_view()),
    url(r'^coordenadasTranvia/(?P<pk>[0-9]+)/$', ConductorTranviaDetail.as_view()),
    url(r'^conductoresMovibus/(?P<pk>[0-9]+)/$', ConductorMoviBusDetail.as_view()),
    url(r'^movibuses/(?P<pk>[0-9]+)/$', MoviBusDetail.as_view()),
    url(r'^coordenadasMovibus/(?P<pk>[0-9]+)/$', ConductorMoviBusDetail.as_view()),
    url(r'^estaciones/(?P<pk>[0-9]+)/$', EstacionVcubsDetail.as_view()),
    url(r'^vcubs/(?P<pk>[0-9]+)/$', VcubsDetail.as_view()),
    url(r'^reportesMovibus/(?P<pk>[0-9]+)/$', ReservaMobiBusDetail.as_view()),
    url(r'^reportesTranvia/(?P<pk>[0-9]+)/$', ReporteTranviaDetail.as_view()),
    url(r'^recorridosMovibus/$', RecorridoMoviBusList.as_view()),
    url(r'^recorridosMovibus/(?P<pk>[0-9]+)/$', RecorridoMoviBusDetail.as_view()),
    url(r'^recorridosTranvia/$', RecorridoTranviaList.as_view()),
    url(r'^recorridosTranvia/(?P<pk>[0-9]+)/$', RecorridoTranviaDetail.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
