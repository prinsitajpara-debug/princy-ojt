from app.auth import hash_password
print('hash short:', hash_password('123456'))
print('hash long:', hash_password('x'*100))
