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

num = int(input("Please enter a number: "))
# num = 2 ** 200 - 1
print(f"{num} is a prime: {is_prime(num)}")