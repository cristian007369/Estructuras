n = int(input("Ingrese el valor de N: ")) #Números perfectos de 1-N
for i in range(1, n + 1):
    vector = [] #Vector para guardar los divisores
    if i % 2 == 0:
        for j in range(1, i // 2 + 1): #Si el n es par, va hasta la n/2 verificando multiplos
            if i % j == 0:
                vector.append(j)
    else:
        for j in range(1, i // 3 + 1): #si el n es impar, va hasta la n/3 verificando multiplos
            if i % j == 0:
                vector.append(j)
    if sum(vector) == i: #Verifica si la suma de sus multiplos es igual al n
        print(f"Número perfecto encontrado: {i}")
        print(vector)
