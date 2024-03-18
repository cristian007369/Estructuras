import random

vector = []
numeros = 1000
imp = 0
par = 0
contimp = 0
conpar = 0

for i in range(1, numeros + 1):
    i=random.randint(1,1001)
    if i%2==0:
        par += i
        conpar += 1
    else:
        imp += i
        contimp +=1
    vector.append(i)

promediopar=par/conpar
promedioimp=imp/contimp

contimp=0

if promediopar>promedioimp:
    for i in vector:
        if i%2==0:
            vector[contimp]=0
        contimp +=1
    print(vector)
else:
    print("Nocas")