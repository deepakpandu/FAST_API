from typing import Union
import jwt  
from fastapi import FastAPI, Request
from pydantic import BaseModel



app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



  
header = {  
  "alg": "HS256",  
  "typ": "JWT"  
}  
  
# payload = {  
#   "sub": "1234567890",  
#   "name": "John Doe",  
#   "iat": 1516239022  
# }  
payload = { 
  "sub": "himdi",  
  "name": "John Doe",  
  "marks": "25"  
}  

  
secret = "Ravipass"  

encoded_jwt = jwt.encode(payload, secret, algorithm='HS256', headers=header)  
print(encoded_jwt)
#decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms=['HS256'])  
#print(decoded_jwt)  

@app.get("/all_data")
def All_data(request:Request):
  authorization_header=request.headers.get("Authorization")
  if authorization_header=="wM4ApimhHgRwWEPCH2PYY2E":
      decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms=['HS256'])    
      return decoded_jwt
  else:
     return 'Not Authorized!'
  