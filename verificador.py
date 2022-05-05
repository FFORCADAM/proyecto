import socket

from rsa import PublicKey

from Cliente import getsha256file
import rsa

archivo=input("Introduce el nombre del archivo que quieres verificar:")
ffirma=open(input("Introduce el fichero que tiene la firma"))
header=1024
versocket= socket.socket()
versocket.connect(('localhost', 9000))

hashh=int(getsha256file(archivo), base=16)

firma=int.from_bytes(ffirma.readline(), byteorder="big")

ffirma.close()

e=int.from_bytes(versocket.recv(header), byteorder="big")
n=int.from_bytes(versocket.recv(header), byteorder="big")

if hashh==firma^e%n:
    print("La firma es válida")
else:
    print("La firma no es válida")
