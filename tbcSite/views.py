from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from usuarios.models import Usuario, ReservaMobiBus
from tranvias.models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia, ReporteTranvia
from movibuses.models import ConductorMoviBus, MoviBus, CoordenadasMoviBus, ReporteMoviBus
from vcubs.models import EstacionVcub, Vcub
from tbcSite.serializers import UsuarioSerializer, ReservaMobiBusSerializer, ConductorTranviaSerializer, TranviaSerializer, LineaSerializer, AlertaTranviaSerializer, CoordenadasTranviaSerializer, ConductorMoviBusSerializer, MoviBusSerializer, CoordenadasMoviBusSerializer, EstacionVcubSerializer, VcubSerializer,ReporteTranviaSerializer, ReporteMoviBusSerializer
from rest_framework import permissions
from tbcSite.permissions import IsOwnerOrReadOnly

class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReservaMobiBusList(generics.ListCreateAPIView):
    queryset = ReservaMobiBus.objects.all()
    serializer_class = ReservaMobiBusSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.Usuario)


class ConductorTranviaList(generics.ListCreateAPIView):
    queryset = ConductorTranvia.objects.all()
    serializer_class = ConductorTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(movibus=self.request.MoviBus)

class TranviaList(generics.ListCreateAPIView):
    queryset = Tranvia.objects.all()
    serializer_class = TranviaSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CoordenadasTranviaList(generics.ListCreateAPIView):
    queryset = CoordenadasTranvia.objects.all()
    serializer_class = CoordenadasTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(tranvia=self.request.Tranvia)

class LineaList(generics.ListCreateAPIView):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AlertaTranviaList(generics.ListCreateAPIView):
    queryset = AlertaTranvia.objects.all()
    serializer_class = AlertaTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(tranvia=self.request.Tranvia)

class ConductorMoviBusList(generics.ListCreateAPIView):
    queryset = ConductorMoviBus.objects.all()
    serializer_class = ConductorMoviBusSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(movibus=self.request.MoviBus)

class MoviBusList(generics.ListCreateAPIView):
    queryset = MoviBus.objects.all()
    serializer_class = MoviBusSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CoordenadasMoviBusList(generics.ListCreateAPIView):
    queryset = CoordenadasMoviBus.objects.all()
    serializer_class = CoordenadasMoviBusSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(movibus=self.request.MoviBus)

class EstacionVcubsList(generics.ListCreateAPIView):
    queryset = EstacionVcub.objects.all()
    serializer_class = EstacionVcubSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VcubsList(generics.ListCreateAPIView):
    queryset = Vcub.objects.all()
    serializer_class = VcubSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save(estacion=self.request.Estacion)

class ReporteMoviBusList(generics.ListCreateAPIView):
    queryset = ReporteMoviBus.objects.all()
    serializer_class = ReporteMoviBusSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReporteTranviaList(generics.ListCreateAPIView):
    queryset = ReporteTranvia.objects.all()
    serializer_class = ReporteTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UsuarioDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ReservaMobiBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservaMobiBus.objects.all()
    serializer_class = ReservaMobiBusSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConductorTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductorTranvia.objects.all()
    serializer_class = ConductorTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class TranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tranvia.objects.all()
    serializer_class = TranviaSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CoordenadasTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoordenadasTranvia.objects.all()
    serializer_class = CoordenadasTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class LineaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AlertaTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlertaTranvia.objects.all()
    serializer_class = AlertaTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConductorMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductorMoviBus.objects.all()
    serializer_class = ConductorMoviBusSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoviBus.objects.all()
    serializer_class = MoviBusSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CoordenadasMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoordenadasMoviBus.objects.all()
    serializer_class = CoordenadasMoviBusSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class EstacionVcubsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstacionVcub.objects.all()
    serializer_class = EstacionVcubSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class VcubsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vcub.objects.all()
    serializer_class = VcubSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ReporteMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReporteMoviBus.objects.all()
    serializer_class = ReporteMoviBusSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ReporteTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReporteTranvia.objects.all()
    serializer_class = ReporteTranviaSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
