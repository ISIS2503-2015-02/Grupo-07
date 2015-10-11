from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from models import EstacionVcub, Vcub
from serializers import EstacionVcubSerializer, VcubSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'tranvia': reverse('tranvia-list', request=request, format=format),
        'alerta': reverse('alerta-list', request=request, format=format),
        'conductor': reverse('alerta-list', request=request, format=format),
        'alerta': reverse('alerta-list', request=request, format=format),
    })



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
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def perform_create(self, serializer):
        serializer.save(estacion=self.request.Estacion)




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
    permission_classes = (permissions.AllowAny,)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
