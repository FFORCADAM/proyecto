import hashlib
import socket
import rsa
from rsa import cli
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


hashh=getsha256file(input("Introduce el nombre del archivo que quieres firmar: "))
print(hashh,"\n")
pub,priv=key.newkeys(2048)
print(pub) #Devuelve n,e
print(priv) #Devuelve n,e,d,p,q
k=OpacityFactorCalculation(n)
k_inverse=common.inverse(k,getattr(pub,'n'))


header=1024
misocket= socket.socket()
misocket.connect(('localhost', 8000))
hash_length=len(str(hashh))
misocket.send(hash_length.to_bytes(length=1024, byteorder="big"))
time.sleep(5)
misocket.send(hashh.to_bytes(length=hash_length, byteorder="big"))
time.sleep(5)
misocket.send(d.to_bytes(length=1024, byteorder="big"))
time.sleep(5)
misocket.send(n.to_bytes(length=1024, byteorder="big"))
time.sleep(5)
firma=int.from_bytes(misocket.recv(header), byteorder="big")
time.sleep(5)
print(firma)
firmafinal=((1/k)*firma)%n
f = open("firma.txt", "w")
f.write(str(firmafinal))
