import time
import jwt
import os
from dotenv import load_dotenv
from uuid import uuid4

dotenv_path = ".env"
load_dotenv(dotenv_path)

app_id      = os.environ.get("APP_ID")
key_file    = os.environ.get("KEY_PATH")
secret      = open(key_file, "r").read()
iat         = int(time.time())
exp         = iat + 3600

payload = dict()
payload.setdefault("application_id", app_id)
payload.setdefault("iat", iat)
payload.setdefault("nbf", iat)
payload.setdefault("exp", exp)
payload.setdefault("jti", str(uuid4()))

token = jwt.encode(payload, secret, algorithm="RS256")

print(token)
