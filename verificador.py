import hashlib
import socket
import time

from rsa import PublicKey


import rsa
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

archivo=input("Introduce el nombre del archivo que quieres verificar:")
ffirma=open(input("Introduce el fichero que tiene la firma:"), encoding="latin-1")
header=1024
versocket= socket.socket()
versocket.connect(('localhost', 8000))

hashh=int(getsha256file(archivo), base=16)
time.sleep(5)
firma=int.from_bytes(bytes(ffirma.readline(), encoding="latin-1"), byteorder="big")

ffirma.close()

e=int.from_bytes(versocket.recv(header), byteorder="big")
time.sleep(5)
n=int.from_bytes(versocket.recv(header), byteorder="big")
time.sleep(5)
x_length=0
versocket.send(x_length.to_bytes(length=1024, byteorder="big"))
comparacion=firma^e%n
if hashh==firma^e%n:
    print("La firma es válida")
else:
    print("La firma no es válida")
    print(hashh)
    print(comparacion)
versocket.close()
