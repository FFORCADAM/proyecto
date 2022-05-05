import socket
import time
from rsa import key


header=1024
pub,priv=key.newkeys(2048)

misocket= socket.socket()
misocket.bind(('localhost', 8000))
misocket.listen(5)
formato= 'utf-8'
while True:
    conexion, addr = misocket.accept()
    print("Conexión establecida")
    conexion.send(pub.e.to_bytes(byteorder="big", length=1024))

    x_length= conexion.recv(header)
    time.sleep(5)
    if x_length:
        print("recibida longitud firma")
        x_length=int.from_bytes(x_length, byteorder="big")
        time.sleep(5)
        print(x_length)
        x = int.from_bytes(conexion.recv(x_length), byteorder="big")
        time.sleep(5)
        print(x)
        print("recibido x")
        d=priv.d
        time.sleep(5)
        n=int.from_bytes(conexion.recv(header), byteorder="big")
        time.sleep(5)
        print("recibida n:" + str(n))
        firmado= (x^d)%n #creo que así se calcula la firma, siendo el "2" el elemento d que no se cual es.
        time.sleep(5)
        conexion.send(firmado.to_bytes(byteorder="big", length=1024))
        conexion.close()
