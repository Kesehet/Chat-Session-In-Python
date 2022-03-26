from replit import db
import string
import random
import json
import time
def setMessage(index,message):
  db["Message_"+index+salt()] = str({"message":message,"time":time.time()})
  pass

def getAllKeysPrefix(index):
  matches = db.prefix("Message_"+index)
  return matches

def getMessage(index):
  x = []
  for ind in getAllKeysPrefix(index):
    x.append(db[ind])
    
    log(0,"Geting Message:- "+str(db[ind])+"From index :- "+ind)    
  delMessage(index)
  return str(x)

def delMessage(index):
  for ind in getAllKeysPrefix(index):
    del db[ind]


def getAllMessage():
  return db.keys()


def log(type,data):
  return
  if type == 0:
    print("Update",":",data)
  elif type == 1:
    print("Warning",":",data)
  elif type == 2:
    print("Error",":",data)
def salt():
  return "_"+''.join(random.choices(string.ascii_uppercase +                            string.digits, k = 12))

try:
  del db["None"]
except:
  pass


def saveKey(person , key):
  db["Key_Getter_"+person] = key
  return "1"
def getKey(person):
  #print("DB KEYS ",db.keys() )
  try:
    return db["Key_Getter_"+person]
  except Exception as e:
    print (e)
    pass
  return "0"
'''client will get the key with the name for any person ... if the name is returned blank ... he writes it as blank ... then checks the size of the text in the file ... if the text length is less than or equal to 1 ... he then tries to save his new key on the server encrypted with a password of his choice ... 

SO lets say Ron opens his client ... he is asked for the person he wants to talk to ... he says Jhon ... the client checks if there is any key with the name Jhon ... he then asks for his password ... Ron enters the password ... that password is used to decrypt Jhons public key ... Jhon had stored this key on the server when he opened the client for the first time ... anyone who has the password of Jhon can access his public key
ron can now use Jhons public key to encrypt text and files and send it to Jhon over the network ... which jhon will be decrypting ... with his private key.




'''