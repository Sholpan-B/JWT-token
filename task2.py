import jwt


def get_payload(token):
    decoded_token = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
    return decoded_token


SECRET_KEY = 'some_secret_key'
token_input = input("Input your token to decode: ")

decoded_payload = get_payload(token_input)
print("Decoded token:", decoded_payload)
