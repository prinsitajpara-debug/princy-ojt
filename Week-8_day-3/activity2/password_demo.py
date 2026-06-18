from passlib.context import CryptContext

# ----------------------------------
# 1. Configure bcrypt
# ----------------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ----------------------------------
# 2. Server-side Pepper
# ----------------------------------

PEPPER = "MySuperSecretPepper"

# ----------------------------------
# 3. Hash Password Function
# ----------------------------------

def hash_password(password: str) -> str:
    password_with_pepper = password + PEPPER
    return pwd_context.hash(password_with_pepper)

# ----------------------------------
# 4. Verify Password Function
# ----------------------------------

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_with_pepper = plain_password + PEPPER
    return pwd_context.verify(
        password_with_pepper,
        hashed_password
    )

# ----------------------------------
# 5. Simulate User Registration
# ----------------------------------

print("=== USER REGISTRATION ===")

user_password = "Admin123"

hashed_password = hash_password(user_password)

print("Original Password:")
print(user_password)

print("\nStored Hash:")
print(hashed_password)

# ----------------------------------
# 6. Simulate Login
# ----------------------------------

print("\n=== LOGIN ATTEMPT ===")

login_password = "Admin123"

if verify_password(login_password, hashed_password):
    print("Login Successful")
else:
    print("Invalid Password")

# ----------------------------------
# 7. Wrong Password Example
# ----------------------------------

print("\n=== WRONG PASSWORD TEST ===")

wrong_password = "WrongPass"

if verify_password(wrong_password, hashed_password):
    print("Login Successful")
else:
    print("Invalid Password")

# ----------------------------------
# 8. API Response Example
# ----------------------------------

print("\n=== API RESPONSE ===")

api_response = {
    "id": 1,
    "username": "john"
}

print(api_response)

# Never do this:
# {
#   "id":1,
#   "username":"john",
#   "password":"$2b$12$..."
# }