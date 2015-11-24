import requests

# verify validation
verify = '/Users/jcbages/Documents/uniandes/arquitecturasw/solumovil/server.pem'

# POST authentication, returns admin token
# so save it in a constant called TOKEN.
URL = 'http://127.0.0.1:8000/api-token-auth/'
data = {
	'username': 'admin',
	'password': '123'
}
ans = requests.post(URL, data=data)
print ans.text.encode('utf8')
ADMIN_TOKEN = ans.json().get('token')

print "=" * 100

# Try to make a GET request without
# being authorized, result should
# be bad (no access).
URL = 'http://127.0.0.1:8000/usuarios/'
ans = requests.get(URL)
print ans.text.encode('utf8')

print "=" * 100

# Add a new user
headers = {
	'Authorization': 'Token %s' % ADMIN_TOKEN
}
data = {
	'nombre': 'Yerson',
	'username': 'yerson',
	'password': '123'
}
ans = requests.post(URL, data=data, headers=headers)
print ans.text.encode('utf8')

print "=" * 100

# Make a GET request now with admin
# token in headers, expect results.
ans = requests.get(URL, headers=headers)
for x in ans.json():
	print x

print "=" * 100

# POST authentication, returns ana token
# so save it in a constant called TOKEN.
URL = 'http://127.0.0.1:8000/api-token-auth/'
data = {
	'username': 'pablo',
	'password': '123'
}
ans = requests.post(URL, data=data, verify=False)
print ans.text.encode('utf8')
ANA_TOKEN = ans.json().get('token')