import json
from base64 import b64encode
import hashlib

import jwt

header = {
    'alg': 'HS256',
    'typ': 'JWT',
}

payload = {
    'sub': 1,
    'birth_date': '17.09.1990',
    'exp': '02.12.2023 23:59',
}


# header = json.dumps(header)
# payload = json.dumps(payload)

SECRET_KEY = 'some_secret_key'

# unsigned_token = b64encode(header) + b'.' + b64encode(payload)

encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
print(encoded_jwt)
