## Para una cantidad definida de números almacenados en un vector, ordenar el vector ascendentemente usando el método burbuja de acuerdo con los siguientes conceptos ##

# 1.	Generar los números randomicos entre 1 y 2000.

# importacion de las librerias
import random
import time

#Ordeamiento burbuja    
def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
            #print(j)



inicio = time.time()

#Creamos la lista
mi_lista = [random.randint(1,2001) for _ in range(12000)]
#print(len(mi_lista))

ordenamiento_burbuja(mi_lista)

fin = time.time()

tiempo_ejecucion = fin - inicio

print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")