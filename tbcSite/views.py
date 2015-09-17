from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from usuarios.models import Usuario, ReservaMobiBus
from tranvias.models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia
from movibuses.models import ConductorMoviBus, MoviBus, CoordenadasMoviBus
from vcubs.models import EstacionVcub, Vcub
from reportes.models import ReporteMoviBus, ReporteTranvia
from tbcSite.serializers import UsuarioSerializer, ReservaMobiBusSerializer, ConductorTranviaSerializer, TranviaSerializer, LineaSerializer, AlertaTranviaSerializer, CoordenadasTranviaSerializer, ConductorMoviBusSerializer, MoviBusSerializer, CoordenadasMoviBusSerializer, EstacionVcubSerializer, VcubSerializer,ReporteTranviaSerializer, ReporteMoviBusSerializer
from rest_framework import permissions

class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReservaMobiBusList(generics.ListCreateAPIView):
    queryset = ReservaMobiBus.objects.all()
    serializer_class = ReservaMobiBusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.Usuario)

class ConductorTranviaList(generics.ListCreateAPIView):
    queryset = ConductorTranvia.objects.all()
    serializer_class = ConductorTranviaSerializer

class TranviaList(generics.ListCreateAPIView):
    queryset = Tranvia.objects.all()
    serializer_class = TranviaSerializer

class CoordenadasTranviaList(generics.ListCreateAPIView):
    queryset = CoordenadasTranvia.objects.all()
    serializer_class = CoordenadasTranviaSerializer

class LineaList(generics.ListCreateAPIView):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer

class AlertaTranviaList(generics.ListCreateAPIView):
    queryset = AlertaTranvia.objects.all()
    serializer_class = AlertaTranviaSerializer

class ConductorMoviBusList(generics.ListCreateAPIView):
    queryset = ConductorMoviBus.objects.all()
    serializer_class = ConductorMoviBusSerializer

class MoviBusList(generics.ListCreateAPIView):
    queryset = MoviBus.objects.all()
    serializer_class = MoviBusSerializer

class CoordenadasMoviBusList(generics.ListCreateAPIView):
    queryset = CoordenadasMoviBus.objects.all()
    serializer_class = CoordenadasMoviBusSerializer

class EstacionVcubsList(generics.ListCreateAPIView):
    queryset = EstacionVcub.objects.all()
    serializer_class = EstacionVcubSerializer

class VcubsList(generics.ListCreateAPIView):
    queryset = Vcub.objects.all()
    serializer_class = VcubSerializer

class ReporteMoviBusList(generics.ListCreateAPIView):
    queryset = ReporteMoviBus.objects.all()
    serializer_class = ReporteMoviBusSerializer

class ReporteTranviaList(generics.ListCreateAPIView):
    queryset = ReporteTranvia.objects.all()
    serializer_class = ReporteTranviaSerializer

class UsuarioDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReservaMobiBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservaMobiBus.objects.all()
    serializer_class = ReservaMobiBusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

class ConductorTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductorTranvia.objects.all()
    serializer_class = ConductorTranviaSerializer

class TranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tranvia.objects.all()
    serializer_class = TranviaSerializer

class CoordenadasTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoordenadasTranvia.objects.all()
    serializer_class = CoordenadasTranviaSerializer

class LineaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer

class AlertaTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlertaTranvia.objects.all()
    serializer_class = AlertaTranviaSerializer

class ConductorMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductorMoviBus.objects.all()
    serializer_class = ConductorMoviBusSerializer

class MoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoviBus.objects.all()
    serializer_class = MoviBusSerializer

class CoordenadasMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoordenadasMoviBus.objects.all()
    serializer_class = CoordenadasMoviBusSerializer

class EstacionVcubsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstacionVcub.objects.all()
    serializer_class = EstacionVcubSerializer

class VcubsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vcub.objects.all()
    serializer_class = VcubSerializer

class ReporteMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReporteMoviBus.objects.all()
    serializer_class = ReporteMoviBusSerializer

class ReporteTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReporteTranvia.objects.all()
    serializer_class = ReporteTranviaSerializer
