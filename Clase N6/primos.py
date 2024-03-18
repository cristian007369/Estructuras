n = int(input("primos en N números "))

vector_primos = [2,3]

for i in range(4,n+1):
    for j in vector_primos:
        if i%j ==0 :
            break
        elif j==vector_primos[-1] and i%j!= 0:
            vector_primos.append(i)
print(len(vector_primos))