import rsa

farch=input("introduce el fichero que quieres verificar")
ffirma=open(input("Introduce el fichero que tiene la firma"))
firma=int(ffirma.readline())

firma_length=len(str(firma))
ffirma.close()
with open(farch, 'rb') as msgfile:
    if len(rsa.verify(msgfile, firma.to_bytes(length=firma_length, byteorder="big"), pubkey))>0:
        print("La firma es válida")
    else:
        print("La firma no es válida")
