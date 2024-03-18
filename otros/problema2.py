import random
import time

n=200000

## Aca esta mi comentario
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def ordenamiento_burbuja2(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

mi_lista = [random.randint(1,2001) for _ in range(n)]
"""mi_lista2 = [random.randint(401,800) for _ in range(int(n/5))]
mi_lista3 = [random.randint(801,1200) for _ in range(int(n/5))]
mi_lista4 = [random.randint(1201,1600) for _ in range(int(n/5))]
mi_lista5 = [random.randint(1601,2000) for _ in range(int(n/5))]
##mi_lista = [x for x in range(1,2001)]

mi_lista = mi_lista1 + mi_lista2 + mi_lista3 + mi_lista4 + mi_lista5
"""
ordenamiento_burbuja2(mi_lista)

inicio = time.time()

mi_lista1 = mi_lista

ordenamiento_burbuja(mi_lista1)

fin = time.time()

tiempo_ejecucion = fin - inicio

print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")