#####################################################################
############## Vectores de numeros impares y ceros ##################
#####################################################################

# Para una cantidad de N numeros randomicos generados entre 1 y 1000, los cuales son alamacenados en un vector, si el promedio de los numeros pares creados es mayor que el de los impares, cambiar a 0 todos los numeros pares y mostrar solo los valores impares al final

# 1. construir la grafica de f(n) del tiempo promedio de generacion para 4 ejecuciones y con el sig tamaño de entrada 
# N=2000, 4000, 8000, 12000, 16000

# Importamos la libreria random
import random
import time

# Guarda el tiempo de inicio
inicio = time.time()

#Definimos variables y el vector
x = []
prom,cont,prom1,cont1 = 0,0,0,0
f= 16000

# Generamos números aleatorios y contamos pares e impares
for i in range(1,f+1):
  i= random.randint(1,f)
  if i%2==0:
    cont = cont+1
    prom =(prom+ i)
      
  else:
    cont1 = cont+1
    prom1 =(prom+ i)
  x.append(i)
  
# Calculamos promedios
par= prom/cont
imp= prom1/cont1

# Imprimimos la lista original

# Definimos una bandera para saber que indice es el que se cambia
bandera=0

# Comparamos los promedios y modificamos la lista si par > imp
if par >= imp:
  for i in x:
    if i%2==0:
      ## Remplazamos los numeros pares por ceros ##
      
      #list.pop([índice])
      x.pop(bandera)
      #list.insert(posición, elemento)
      x.insert(bandera,0)
    bandera += 1

  print(x)
else:
  print("Nocas")
  

# Guarda el tiempo de finalización
fin = time.time()

# Calcula el tiempo de ejecución
tiempo_ejecucion = fin - inicio

print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")