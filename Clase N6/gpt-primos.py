def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

primes_under_100000 = sieve_of_eratosthenes(100000)
print("Cantidad de números primos antes de 100,000:", len(primes_under_100000))
