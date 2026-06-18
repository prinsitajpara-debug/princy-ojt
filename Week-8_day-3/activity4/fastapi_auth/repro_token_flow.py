import urllib.request, urllib.parse, json

# register
url = 'http://127.0.0.1:8000/auth/register'
data = json.dumps({'name':'TokenUser3','email':'tokenuser3@example.com','password':'123456'}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type':'application/json'})
with urllib.request.urlopen(req, timeout=10) as resp:
    print('REGISTER', resp.status, resp.read().decode())

# login via form data
url = 'http://127.0.0.1:8000/auth/login'
form = urllib.parse.urlencode({'username':'tokenuser3@example.com','password':'123456'}).encode('utf-8')
req = urllib.request.Request(url, data=form, headers={'Content-Type':'application/x-www-form-urlencoded'})
with urllib.request.urlopen(req, timeout=10) as resp:
    body = resp.read().decode()
    print('LOGIN', resp.status, body)
    token = json.loads(body)['access_token']

# call protected endpoint
url = 'http://127.0.0.1:8000/auth/me'
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}'})
with urllib.request.urlopen(req, timeout=10) as resp:
    print('ME', resp.status, resp.read().decode())
