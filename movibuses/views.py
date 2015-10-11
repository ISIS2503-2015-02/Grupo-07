from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from models import ConductorMoviBus, MoviBus, CoordenadasMoviBus, ReporteMoviBus
from serializers import ConductorMoviBusSerializer, MoviBusSerializer, CoordenadasMoviBusSerializer,ReporteMoviBusSerializer
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route
from rest_framework import renderers

class ConductorMoviBusList(generics.ListCreateAPIView):
    queryset = ConductorMoviBus.objects.all()
    serializer_class = ConductorMoviBusSerializer
    permission_classes = (permissions.AllowAny,)
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
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(movibus=self.request.MoviBus)

class ReporteMoviBusList(generics.ListCreateAPIView):
    queryset = ReporteMoviBus.objects.all()
    serializer_class = ReporteMoviBusSerializer
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ConductorMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConductorMoviBus.objects.all()
    serializer_class = ConductorMoviBusSerializer
    permission_classes = (permissions.AllowAny)
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
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ReporteMoviBusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReporteMoviBus.objects.all()
    serializer_class = ReporteMoviBusSerializer
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
