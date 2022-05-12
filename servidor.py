import socket
import time
from rsa import key
from rsa import PublicKey, PrivateKey
header=1024
pub,priv=key.newkeys(2048)

try:
    pubkey=PublicKey._load_pkcs1_pem(open("pubKey.pem", "rb").read())
    print("Obtenemos del archivo pubKey.pem la clave pública")
    e=pubkey.e
    n=pubkey.n
    privkey=PrivateKey._load_pkcs1_pem(open("privKey.pem", "rb").read())
    d=privkey.d
except IOError:
    print('El servidor no se ha ejecutado nunca o se ha movido el fichero de la clave pública de sitio. Procedemos a crear el archivo pubKey.pem para guardar la clave pública disponible aun con el servidor apagado ')
    with open("pubKey.pem", "wb") as q:
        q.write(PublicKey._save_pkcs1_pem(pub))
        e=pub.e
        n=pub.n
        q.close()
    with open("privKey.pem", "wb") as p:
        p.write(PrivateKey._save_pkcs1_pem(priv))
        d=priv.d
        p.close()
misocket= socket.socket()
misocket.bind(('localhost', 8000))
misocket.listen(5)
while True:
    conexion, addr = misocket.accept()
    print("Conexión establecida")
    x_length= int.from_bytes(conexion.recv(header), byteorder="big")
    time.sleep(1)
    if x_length:
        print("recibida longitud firma de parte del cliente")
        #time.sleep(1)
        x = int.from_bytes(conexion.recv(x_length), byteorder="big")
        time.sleep(1)
        print(x)
        print("Recibido el hash cegado")
        time.sleep(1)
        print("Realizamos la firma")
        firmado=pow(x,d,n)
        time.sleep(1)
        conexion.send(firmado.to_bytes(byteorder="big", length=1024))
        print("Se completó la operación con exito, se cierra la conexión")
        conexion.close()

