import time

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

contraseña = str(input("Contraseña: "))

ban = 0

inicio = time.time()

def buscar_contraseña():
    for i in alphabet:
        for ii in numbers:
            for iii in alphabet:
                for iiii in numbers:
                    con = i + ii + iii + iiii
                    if con == contraseña:
                        return con  # Retorna la contraseña encontrada
                    ban += 1

contraseña_encontrada = buscar_contraseña()

if contraseña_encontrada:
    print(contraseña_encontrada)
else:
    print("La contraseña no se encontró.")

final = time.time()
tiempo = final - inicio
print(f"contraseña encontrada en {ban} intentos y en {tiempo} s")
