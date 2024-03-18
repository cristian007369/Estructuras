m1000 = int(input("Cantidad de 1000: "))
m500 = int(input("Cantidad de 500: "))
m200 = int(input("Cantidad de 200: "))
m100 = int(input("Cantidad de 100: "))
m50 = int(input("Cantidad de 50: "))

vueltos = int(input("Cantidad a devolver: "))

v1000 = 0
v500 = 0
v200 = 0
v100 = 0
v50 = 0

if vueltos//1000 <= m1000:
    v1000 = vueltos//1000
else:
    v1000 = m1000

if (vueltos - v1000*1000)//500 > m500:
    v500 = m500
else:
    v500 = (vueltos - v1000*1000)//500

if (vueltos -v1000*1000 -v500*500)//200 <= m200:
    v200 = (vueltos -v1000*1000 -v500*500)//200
else:
    v200 = m200

if (vueltos -v1000*1000 -v500*500 -v200*200)//100 <= m100:
    v100 = (vueltos -v1000*1000 -v500*500 -v200*200)//100
else:
    v100 = m100

if (vueltos -v1000*1000 -v500*500 -v200*200 -v100*100)//50 <= m50:
    v50 = (vueltos -v1000*1000 -v500*500 -v200*200 -v100*100)//50
else:
    v50 = m50

if v1000*1000 + v500*500 + v200*200 +v100*100 +v50*50 == vueltos:
    print(f"dar {v1000} de 1000, {v500} de 500, {v200} de 200, {v100} de 100 y {v50} de 50")
else:
    print("No hay plata suficiente")