import jwt


def create_token(username):
    payload = {'username': username}
    encoded_jwt = jwt.encode(payload, 'SECRET_KEY', algorithm='HS256')
    return encoded_jwt


SECRET_KEY = 'some_secret_key'
username = input("Enter your username: ")
encoded_jwt = create_token(username)
print("JWT token:", encoded_jwt)
