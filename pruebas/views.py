from django.http import HttpResponse
from django.views.generic import View
from django.core import serializers
from django.http import QueryDict

cache = {}

# Create your views here.
class CacheView(View):

	# POST view
	def post(self, request):
		k1, k2, k3 = obtenerDatos(request.POST)
		b = Bus(datos)
		b.save()
		data = serializers.serialize("json", b)
		return HttpResponse(data)

	# GET view
	def get(self, request, pk=-1):
		if pk != -1:
			data = serializers.serialize("json", Bus.objects.get(pk=pk))
		else:
			data = serializers.serialize("json", Bus.objects.all())
		return HttpResponse(data)

	# PUT view
	def put(self, request, pk=-1):
		k1, k2, k3 = obtenerDatos(request.body)
		if pk != -1:
			b = Bus.objects.all(pk=pk)
			b.k1 = k1
			b.k2 = k2
			# ...
			b.save()
			return HttpResponse(b)
		else:
			return HttpResponse(status=403)


	# DELETE view
	def delete(self, request):
		print request
		return HttpResponse("")
