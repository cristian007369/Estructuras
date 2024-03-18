import random
import time
import sys

sys.setrecursionlimit(200000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

vector = []
vector1 =[]
n = 500000
suma = 0
contador = 0

tiempo1 = time.time()

while contador<=n:
    x = random.randint(0,100)
    if x%2 ==0:
        vector.append(x)
        suma += x
    contador += 1
y= len(vector)
promedio = suma/y if y > 0 else 0

for i in vector:
    if i < promedio:
        vector1.append(i)

if n/2 > len(vector1):
    resultado = quicksort(vector1)
else:
    print("Nocas")

timepo2 = time.time()
tiempoeje = timepo2-tiempo1
print(tiempoeje)