#importacion de las librerias necesarias

import random
import time

#funcion para convertir a binario

def fbinario(numero):
    binario = ''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    ##print(f"Número original: {num}, Binario: {binario}")

"""def fbinario(numero):
    return bin(numero)[2:] if numero >= 0 else '-' + bin(-numero)[2:]
"""

#genereacion del vector
n = int(input("cuantos numeros tendra el vector: "))

vector_tiempos = []

# lis = int(input("cuantos digitos tendra la lista: "))
# n = 0
# while n < lis:
#   nu = list(input("numeros: "))
#   n = n + 1
# inicio del conteo del tiempo
for _ in range(4):
    start_time = time.time()
    vector = [random.randint(1001, 10000) for i in range(n)]
    # vector = [nu]
    #convertir a binario los numeros del vector

    for num in vector:
        fbinario(num)

    #fin del conteo del tiempo

    end_time = time.time()
    tiempo = end_time - start_time
    vector_tiempos.append(tiempo)

"""
for _ in range(6):
    n = int(input("Número: "))
    binario = fbinario(n)
    print(binario)
#impresion del tiempo
"""
print(vector_tiempos)
print(n)