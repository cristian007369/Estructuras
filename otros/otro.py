import random

vector = []
numeros = 1000
imp = 0
par = 0
contimp = 0
conpar = 0

# Llenar la lista y calcular sumas
for _ in range(numeros):
    i = random.randint(1, 1001)
    vector.append(i)
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

print(vector)
