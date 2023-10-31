def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False
    return [x for x in range(2, limit + 1) if sieve[x]]

limit = 10000000  # Állítsd be a kívánt limitet itt
primes = sieve_of_eratosthenes(limit)
 
# for prime in primes:
#     print(prime)

print(len(primes))
