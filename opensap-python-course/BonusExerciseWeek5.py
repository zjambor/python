"""
Write a program, that gets an integer through input and creates a list containing all prime numbers until this input. To do so, two functions have to be implemented:

    The function is_prime() gets an integer as input and returns True if this integer is prime, and False if the integer is not prime.
    The function prime_list() gets an integer as input and checks each number from 2 to input, if it is prime by calling the above function. If a number is prime, it is appended to a list. This list is given back as the return value of prime_list().

The program finally outputs the list of all prime numbers.
"""

def is_divisible(a, b):
    """
    Checks if a is divisible by b without a remainder
    """
    return a % b == 0

def is_prime(n):
    """
    Checks if the number n is a prime number
    """
    for i in range(2, n):
        if is_divisible(n, i):
            return False
    return True

def prime_list(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

max_prime = int(input("Up to which number do you want all prime numbers: "))
print(prime_list(max_prime))
