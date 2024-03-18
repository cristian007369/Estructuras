import math

n = int(input("Ingrese el valor de N: "))
for i in range(1, n + 1):
    vector = []
    limit = int(math.sqrt(i)) + 1
    for j in range(1, limit):
        if i % j == 0:
            vector.append(j)
            if j != i // j:
                vector.append(i // j)
    if sum(vector) - i == i:
        print(f"Número perfecto encontrado: {i}")

def divisores():
    for i in range(1, n+1):
        vector_primos = []
        for j in range(1,i+1):
            if i%j ==0:
                vector_primos.append(j)
        print(vector_primos)