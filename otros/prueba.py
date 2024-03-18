import random
import time
    
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

x=[]
arr=[]
l = len(x)
n = 15000
rta=0

#lista de numeros randomicos pares
inicio = time.time()

while (l<n):
    num = random.randint(1,100)
    if num %2 == 0:
        x.append(num)
    l = len(x)
#print(x)

#verificar numeros y promedio
prom = sum(x)/len(x)
#print(prom)
for i in x:
    if i < prom:
        arr.append(i)
#print(arr)

#Conteo menor que n/2?
cont=len(arr)
if cont < (n/2):
    rta= quicksort(arr)
else:
    rta = f"{cont} no es menor que {n/2}"
print(rta)

fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")