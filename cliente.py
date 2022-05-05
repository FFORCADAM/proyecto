import hashlib
import socket
import time
from math import gcd
import random

import rsa
from rsa import cli, common
from rsa import key
from rsa import prime

#Calcula el hash

def getsha256file(archivo):
    try:
        hashsha = hashlib.sha256()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashsha.update(bloque)
        return hashsha.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""


def OpacityFactorCalculation(n):
    k=random.randint(2, n-1)
    while gcd(k,n)!=1:
        k=random.randint(0, n-1)
    return k


hashh=int(getsha256file(input("Introduce el nombre del archivo que quieres firmar: ")), base=16)
print(hashh,"\n")
pub,priv=key.newkeys(2048)

n=priv.n
k=OpacityFactorCalculation(n)
k_inverse=common.inverse(k,getattr(pub,'n'))


header=1024
misocket= socket.socket()
misocket.connect(('localhost', 8000))

e=int.from_bytes(misocket.recv(header), byteorder="big")
time.sleep(5)
x=((k^e)*hashh)%n
x_length=len(str(x))
time.sleep(5)
misocket.send(x_length.to_bytes(length=1024, byteorder="big"))
time.sleep(5)
misocket.send(x.to_bytes(length=x_length, byteorder="big"))
time.sleep(5)
misocket.send(n.to_bytes(length=1024, byteorder="big"))
time.sleep(5)
firma=int.from_bytes(misocket.recv(header), byteorder="big")
time.sleep(5)
print(firma)
firmafinal=float(((k_inverse)*firma)%n)

with open("firma.pem", "wb") as f:
    f.write(firmafinal)
    f.close()
 
with open("c_pública.pem", "wb") as q:
    q.write(publica) #No sabemos bien qué enviar
    q.close()

