import random
import time

inicio = time.time()

vector = [random.randint(1,1001) for _ in range(16000000)]
imp = 0
par = 0
contimp = 0
conpar = 0

# Llenar la lista y calcular sumas
for i in vector:
    if i % 2 == 0:
        par += i
        conpar += 1
    else:
        imp += i
        contimp += 1

# Calcular promedios
promediopar = par / conpar if conpar > 0 else 0
promedioimp = imp / contimp if contimp > 0 else 0

# Modificar los valores del vector según la comparación de promedios
if promediopar > promedioimp:
    vector = [0 if x % 2 == 0 else x for x in vector]
else:
    print("No marica")

print(vector)

fin = time.time()

tiempo_ejecucion = fin - inicio

print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")