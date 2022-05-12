import hashlib
import socket
import time
from math import gcd
import random
from rsa import common
from rsa import PublicKey


# Calcula el hash

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
    k = random.randint(2, n - 1)
    while gcd(k, n) != 1:
        k = random.randint(0, n - 1)
    return k

hashh = int(getsha256file(input("Introduce el nombre del archivo que quieres firmar: ")), base=16)
print("El cliente calcula el hash del archivo.")
header = 1024
misocket = socket.socket()
misocket.connect(('localhost', 8000))
print("El cliente ha obtenido la clave pública del servidor y ciega el hash a partir de ella.")
pubkey = PublicKey._load_pkcs1_pem(open("pubKey.pem", "rb").read())
e = pubkey.e
n = pubkey.n
k = OpacityFactorCalculation(n)
k_inverse = common.inverse(k, n)
x = (hashh * pow(k, e, n)) % n
x_length = len(str(x))
time.sleep(1)
misocket.send(x_length.to_bytes(length=1024, byteorder="big"))
print("Mandamos el hash cegado a servidor")
time.sleep(1)
misocket.send(x.to_bytes(length=x_length, byteorder="big"))
time.sleep(1)
firma = int.from_bytes(misocket.recv(header), byteorder="big")
time.sleep(1)
print("Recibimos la firma cegada. Procedemos a descegarla.")
firmafinal = ((k_inverse) * firma) % n
nombre_final=input("Introduce el nombre del archivo donde quieras guardar la firma en formato .txt (Se guardará en el directorio donde están los programas): ")
with open(nombre_final, "w") as f:
    f.write(str(firmafinal))
    f.close()
misocket.close()
