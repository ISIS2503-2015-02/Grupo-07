import requests
import json
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

OAUTH_POLICY = 'https://api.stormpath.com/v1/applications/dt2VrW0681I4hVSLUmuzb/oauth/token'

class Auth(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello Me')

	def post(self, request, *args, **kwargs):
		auth = (settings.STORMPATH_ID, settings.STORMPATH_SECRET)
		data = request.POST.copy()
		data['grant_type'] = 'password'
		ans = requests.post(OAUTH_POLICY, auth=auth, data=data).json()
		return HttpResponse(json.dumps(ans), content_type='application/json')