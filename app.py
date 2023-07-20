from typing import Union
import jwt  
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

header = {  
    "alg": "HS256",  
    "typ": "JWT"  
}

payload = { 
    "sub": "himdi",  
    "name": "John Doe",  
    "marks": "25"  
}

secret = "Ravipass"

encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)
print(encoded_jwt)

@app.get("/all_data")
def All_data(request: Request):
    authorization_header = request.headers.get("Authorization")
    if authorization_header == "wM4ApimhHgRwWEPCH2PYY2E":  
        decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms=['HS256'])
        return decoded_jwt
    else:
        return 'Not Authorized!'
