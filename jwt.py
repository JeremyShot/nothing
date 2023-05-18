import base64
import hmac
import time
import json


KEY = '257g2v4*nk456)&*GPI89H(Y7t3475h%^$@#$drjmniu345983nc4u9'
EXP = 60*60*24*7
ALG = 'HS256' 

class my_jwt:
  
  @staticmethod
  def generate_token(username = 'Roieee',id = "v54g643ertyrtyh3546vbxc545wvbw544564ret35b546df",age = 21,department = "akbfginadofmroit"):
    #init header
    header = {
      "alg":ALG,
      "typ":"JWT"
    }

    header_json = json.dumps(header).encode("utf-8")
    header_json_base64 = base64.urlsafe_b64encode(header_json).replace(b"=",b"")
    
    #init payload
    payload = {
      #registered claims
      "exp": time.time() + EXP,
      "iss": "Jeremy",

      #private claims
      "p_username":username,
      "p_id":id,
      "p_age":age,
      "p_department":department
    }

    payload_json = json.dumps(payload).encode("utf-8")
    payload_json_base64 = base64.urlsafe_b64encode(payload_json).replace(b"=",b"")

    #init signature
    hm = hmac.new(KEY.encode('utf-8'),header_json_base64 + b"." + payload_json_base64,digestmod = "SHA256")
    hm_base64 = base64.urlsafe_b64encode(hm.digest()).replace(b"=",b"")
    
    return header_json_base64 + b"." + payload_json_base64 + b"." + hm_base64

  @staticmethod
  def b64encode(json_str):
    return base64.urlsafe_b64encode(json_str).replace(b"=",b"")
  
  @staticmethod
  def b64decode(b_json):
    rem = len(b_json) % 4
    if(rem > 0):
      b_json += b"=" * (4 - rem)
    return base64.urlsafe_b64decode(b_json)
    

  @staticmethod
  def decrypt_token(token,KEY):
     header_b,payload_b,signature_b = token.split(b".")
     hm = hmac.new(KEY.encode('utf-8'),header_b + b"." + payload_b,digestmod = "SHA256")
     hm_base64 = base64.urlsafe_b64encode(hm.digest()).replace(b"=",b"")

     if hm_base64 != signature_b:
       raise "Signature failed"
     '''else:
       print("Not expired")
     '''
     rem = len(payload_b) % 4
     if(rem > 0):
       payload_b += b"=" * (4 - rem)
     payload_j = base64.urlsafe_b64decode(payload_b)
     payload = json.loads(payload_j)
     if(time.time() > payload['exp']):
       raise "User expired"
     return payload



if __name__  == '__main__':
  #test
  jwt_token = my_jwt.generate_token()
  print(jwt_token)
  payload = my_jwt.decrypt_token(b'''eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODQ4ODg4ODguMDkwNzc0OCwiaXNzIjoiUm9pZWVlIiwicF91c2VybmFtZSI6InNoaWJhIiwicF9pZCI6IjEyMzQ1NjciLCJwX2FnZSI6NDMsInBfZGVwYXJ0bWVudCI6ImFzZGdlZyJ9.0kfrsCo2W_N7O1GbLu78bTt5KGT6um0mnw48kOc2Od0''',KEY)
  print(payload)

  
    