def factorial_n(n,iter):
    iter2 = iter - 1
    n2 = n-1
    if n2 >= 1 or iter2>0:
        n = n * factorial_n(n2,iter2)
    return n

def factorial_n1(n,iter):
    iter += 1
    n2 = n-1
    if n2 > 1 :
        n = n * factorial_n1(n2,iter)
    return iter

n = int(input("Dígite un númerro: "))
n_iter = 0


while n<0:
    n = int(input("Dígite un númerro: "))

x = factorial_n1(n,n_iter)

n_iter = int(input(f"Dígite en que iteracción parar entre 1-{x}: "))

while n_iter<0 and n_iter>=n-x:
    n_iter = int(input(f"Dígite en que iteracción parar entre 1-{n-x}: "))

x = factorial_n1(n,n_iter)

print(f"Factorial parcial es  {x}")