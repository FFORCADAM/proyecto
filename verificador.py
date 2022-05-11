import hashlib
from rsa import PublicKey

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
clavepub=open("pubKey.pem", "rb")
pubkey=PublicKey._load_pkcs1_pem(clavepub.read())
e=pubkey.e
n=pubkey.n
firma=(int.from_bytes(bytes(ffirma.read().lstrip(), encoding="latin-1"), byteorder="big"))%n
ffirma.close()
hashh=(int(getsha256file(archivo), base=16))%n
comparacion=pow(firma,e,n)
if hashh==comparacion:
    print("La firma es válida")
else:
    print("La firma no es válida")
    print(hashh)
    print(comparacion)
clavepub.close()
