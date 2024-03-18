import time

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

contraseña = str(input("Contraseña: "))

contraseña = list(contraseña)

if contraseña[0] in alphabet and contraseña[1] in numbers and contraseña[2] in numbers and contraseña[3] in alphabet:

    inicio = time.time()

    def encontrar_contraseña():
        ban = 0
        for i in alphabet:
            for ii in numbers:
                for iii in numbers:
                    for iiii in alphabet:
                        con = i+ii+iii+iiii
                        ban += 1
                        if con == contraseña:
                            print(f"Número de intentos: {ban}")
                            return con

    cont_encontrada = encontrar_contraseña()

    final = time.time()

    tiempo = final - inicio

    print(f"contraseña encontrada en {tiempo} s")
else:
    print("Contraseña no valida")