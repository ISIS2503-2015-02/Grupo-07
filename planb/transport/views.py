from django.core import serializers
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.generic import View

import json
from .models import *

# Handles Transport model CRUD
class TransportView(View):

	# GET (DONE)
	# Used for getting all transports
	# or a single one in the system.
	def get(self, request, pk=''):
		if pk:
			try:
				t = Transport.objects.get(pk=pk)
				ans = serializers.serialize('json', [t,])
				return HttpResponse(ans, status=200)
			except:
				ans = json.dumps({ "error": "No record found for pk=%s." % pk })
				return HttpResponse(ans, status=404)
		else:
			t = Transport.objects.all()
			ans = serializers.serialize('json', t)
			return HttpResponse(ans, status=200)

	# POST (DONE)
	# Used for adding a new transport
	# to the system. 
	def post(self, request, pk=''):
		if pk:
			ans = json.dumps({ "error": "No pk allowed in POST." })
			return HttpResponse(ans, status=403)
		else:
			try:
				data = QueryDict(request.body)
				driver_name = data.get('driver_name')[0]
				license_plate = data.get('license_plate')[0]
				transport_type = data.get('transport_type')[0]
				t = Transport(
					driver_name=driver_name,
					license_plate=license_plate,
					transport_type=transport_type,
					transport_status=0
				)
				t.save()
				ans = serializers.serialize('json', [t,])
				return HttpResponse(ans, status=200)
			except:
				ans = json.dumps({ "error": "POST data is not complete." })
				return HttpResponse(ans, status=403)

	# PUT
	# Used for update transport status
	# if some accident occurs.
	def put(self, request, pk=''):
		if pk:
			t = Transport.objects.get(pk=pk)
			# Edit data...
			t.save()
			ans = serializers.serialize('json', [t,])
			return HttpResponse(ans, status=200)
		else:
			ans = json.dumps({ "error": "PUT requires pk." })
			return HttpResponse(ans, status=403)
		
# Handles Historic model CRUD
class HistoricView(View):

	# GET (DONE)
	# Used for getting the historical
	# route and tracing the map of all
	# transports or an specific one.
	def get(self, request, transport_pk=''):
		if transport_pk:
			try:
				print "Trying with transport_pk", transport_pk
				h = Historic.objects.filter(transport_pk_id=transport_pk)
				ans = serializers.serialize('json', h)
				return HttpResponse(ans, status=200)
			except:
				ans = json.dumps({ "error": "No record found for transport_pk=%s." % transport_pk })
				return HttpResponse(ans, status=404)
		else:
			h = Historic.objects.all()
			ans = serializers.serialize('json', h)
			return HttpResponse(ans, status=200)

	# POST (DONE)
	# Used for adding a new position
	# of some transport.
	def post(self, request, transport_pk=''):
		if transport_pk:
			ans = json.dumps({ "error": "No pk allowed in POST." })
			return HttpResponse(ans, status=403)
		else:
			try:
				data = QueryDict(request.body)
				transport_pk = data.get('transport_pk')
				latitude_pos = data.get('latitude_pos')
				longitude_pos = data.get('longitude_pos')
				transport_speed = data.get('transport_speed')
				h = Historic(
					transport_pk_id=transport_pk,
					latitude_pos = latitude_pos,
					longitude_pos = longitude_pos,
					transport_speed = transport_speed
				)
				h.save()
				ans = serializers.serialize('json', [h,])
				return HttpResponse(ans, status=200)
			except:
				ans = json.dumps({ "error": "POST data is not complete." })
				return HttpResponse(ans, status=403)

