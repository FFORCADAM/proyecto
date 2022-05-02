import hashlib
import socket
import random


first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

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

#Elegimos un candidato principal aleatorio
def nBitRandom(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)

#Nos aseguramos de que el candidato no es divisible por los primeros números primos
def getLowLevelPrime(n):
    while True:

        prime_candidate = nBitRandom(n)

        for divisor in first_primes_list:
            if prime_candidate % divisor == 0 and divisor ** 2 <= prime_candidate:
                break
        else:
            return prime_candidate

#Prueba de Rabin Miller
def isMillerRabinPassed(miller_rabin_candidate):
    maxDivisionsByTwo = 0
    even_component = miller_rabin_candidate - 1
    while even_component % 2 == 0:
        even_component >>= 1
        maxDivisionsByTwo += 1
    assert (2 ** maxDivisionsByTwo * even_component == miller_rabin_candidate - 1)

    def trialComposite(round_tester):
        if pow(round_tester, even_component, miller_rabin_candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2 ** i * even_component, miller_rabin_candidate) == miller_rabin_candidate - 1:
                return False
        return True

    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    return True


n = 1024
vector=[]
while len(vector)<2:
    prime_candidate = getLowLevelPrime(n)
    if isMillerRabinPassed(prime_candidate):
        vector.append(prime_candidate)
p=vector[0]
q=vector[1]
n=p*q
print(p,"\n")
print(q,"\n")
print(n)


header=1024
misocket= socket.socket()
misocket.connect(('localhost', 8000))

hashh=125423453245 #implementar calculo hash
n=123451235125 #implementar calculo n
d=234532452 #implementar calculo d
hash_length=len(str(hashh))
misocket.send(hash_length.to_bytes(length=1024, byteorder="big"))
misocket.send(hashh.to_bytes(length=hash_length, byteorder="big"))
misocket.send(d.to_bytes(length=1024, byteorder="big"))
misocket.send(n.to_bytes(length=1024, byteorder="big"))
firma=int.from_bytes(misocket.recv(header), byteorder="big")
print(firma)
