import jwt
import datetime
from datetime import timezone


def create_token(username):
    access_exp = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=30)
    refresh_exp = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=30)

    access_token = jwt.encode({'exp': access_exp, 'username': username}, 'secret_key', algorithm='HS256')
    refresh_token = jwt.encode({'exp': refresh_exp, 'username': username}, 'secret_key', algorithm='HS256')

    return {'access_token': access_token, 'refresh_token': refresh_token}


username = input("Input your username: ")
tokens = create_token(username)

print("Your access token:", tokens['access_token'])
print("Your refresh token:", tokens['refresh_token'])
