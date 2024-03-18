f = open("archivo.txt", "r")
texto = f.read()

palabra_buscar = str(input("Dígite la palabra a buscar: ")).lower()#Usuario ingresa una palabra

palabra=list(palabra_buscar)#Crea una lista con la palabra

cont = 0

for i in texto:#Itera sobre el texto

    if palabra[cont] == i:#Agrega +1 si hay una coincidencia de letras
        cont += 1
    else:#si no da el valor de 0 a cont
        cont = 0
    if cont == len(palabra):#Si el valor de cont("contador") es igual al largo de la palabra
                            #quiere decir que la encontro
        print("palabra encontrada")
        break

if cont == 0:#los unicos dos valores para cot es 0 o el largo de la palabra
    print("No se encontro la palabra")

f.close()