def is_divisible(a, b):
    """
    Checks if a is divisible by b without a remainder
    """
    return a % b == 0

# traditional function
def is_prime(n):
    """
    Checks if the number n is a prime number
    """
    for i in range(2, n):
        if is_divisible(n, i):
            return False
    return True

# quick function
def isPrime(n):
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

num = int(input("Please enter a number: "))
# num = 2 ** 200 - 1
print(f"{num} is a prime: {isPrime(num)}")
# pl. 595944331
