from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
resp = client.post('/auth/register', json={'name':'Prinsi','email':'prinsi@gmail.com','password':'123456'})
print('status', resp.status_code)
print('text:', resp.text)
print('headers:', resp.headers)
try:
    print('json:', resp.json())
except Exception as e:
    print('json error', e)
