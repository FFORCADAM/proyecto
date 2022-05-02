import socket

header=1024
misocket= socket.socket()
misocket.bind(('localhost', 8000))
misocket.listen(5)
formato= 'utf-8'
while True:
    conexion, addr = misocket.accept()
    print("Conexión establecida")
    firma_length= conexion.recv(header)
    if firma_length:
        print("recibida longitud firma")
        firma_length=int.from_bytes(firma_length, byteorder="big")
        print(firma_length)
        firma = int.from_bytes(conexion.recv(firma_length), byteorder="big")
        print(firma)
        print("recibida firma")
        d=int.from_bytes(conexion.recv(header), byteorder="big")
        print("recibida d:"+ str(d))
        n=int.from_bytes(conexion.recv(header), byteorder="big")
        print("recibida n:" + str(n))
        firmado= (firma^d)%n #creo que así se calcula la firma, siendo el "2" el elemento d que no se cual es.
        conexion.send(firmado.to_bytes(byteorder="big", length=256))
        conexion.close()
