from django.http import HttpResponse
from django.views.generic import View

from .models import BusPrueba

cache = []

# Create your views here.
class CacheView(View):
	def post(self, request):
		msg = "Soy la rta de cache"
		if (len(cache) > 0): cache[0] = msg
		else: cache.append(msg)
		return HttpResponse(cache[0])
	def get(self, request):
		msg = "No hay"
		if (len(cache) > 0): msg = cache[0]
		return HttpResponse(msg)

class DBView(View):
	def post(self, request):
		b = BusPrueba(msg="Soy la rta de bus1")
		b.save()
		return HttpResponse(b.msg)
	def get(self, request):
		msg = "No hay"
		all_ent = BusPrueba.objects.all()
		if len(all_ent) > 0: msg = all_ent[0].msg
		return HttpResponse(msg)