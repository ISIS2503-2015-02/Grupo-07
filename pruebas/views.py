from django.http import HttpResponse
from django.views.generic import View
from django.core import serializers
from django.http import QueryDict
from movibuses.models import MoviBus
import requests

cache = {}

# Create your views here.
class CacheView(View):

	# POST view
	def post(self, request):
		for deserialized_object in serializers.deserialize("json", request.POST[ ]):
		    deserialized_object.save();
		return HttpResponse(deserialized_object);

	# GET view
	def get(self, request, ide=-1):
		if ide != -1:
			data = serializers.serialize("json", [MoviBus.objects.get(pk=ide),])
		else:
			data = serializers.serialize("json", [MoviBus.objects.all(),])
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
