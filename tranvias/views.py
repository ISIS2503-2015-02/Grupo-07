from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia, ReporteTranvia
from serializers import ConductorTranviaSerializer, TranviaSerializer, LineaSerializer, AlertaTranviaSerializer, CoordenadasTranviaSerializer, ReporteTranviaSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ConductorTranviaList(generics.ListCreateAPIView):
    queryset = ConductorTranvia.objects.all()
    serializer_class = ConductorTranviaSerializer
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(tranvia=self.request.MoviBus)

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
    permission_classes = (permissions.AllowAny,)
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
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(tranvia=self.request.Tranvia)

class ReporteTranviaList(generics.ListCreateAPIView):
    queryset = ReporteTranvia.objects.all()
    serializer_class = ReporteTranviaSerializer
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConductorTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductorTranvia.objects.all()
    serializer_class = ConductorTranviaSerializer
    permission_classes = (permissions.AllowAny,)
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
    permission_classes = (permissions.AllowAny,)
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
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReporteTranviaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReporteTranvia.objects.all()
    serializer_class = ReporteTranviaSerializer
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
