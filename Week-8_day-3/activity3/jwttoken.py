from jose import jwt
from jose.exceptions import ExpiredSignatureError
from datetime import datetime, timedelta

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

payload = {
    "sub": "1",
    "type": "access",
    "iat": datetime.utcnow(),
    "exp": datetime.utcnow() + timedelta(minutes=1)
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm=ALGORITHM
)

print("TOKEN:")
print(token)

try:
    decoded = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    print("\nDECODED:")
    print(decoded)

except ExpiredSignatureError:
    print("Token expired")