import time
import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

contraseña = str(input("Contraseña: "))

ban = 0

inicio = time.time()

while True:
    a1 = random.choice(alphabet)
    a2 = random.choice(numbers)
    a3 = random.choice(numbers)
    a4 = random.choice(alphabet)
    cont = a1 + a2 +a3 + a4
    ban += 1
    if cont == contraseña:
        break

final = time.time()
tiempo = final - inicio
print(f"contraseña encontrada en {ban} intentos y en {tiempo} s")