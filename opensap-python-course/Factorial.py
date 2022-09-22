# recursive way

def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n - 1) * n

for i in range(1, 6):
    print(f"Factorial of {i} is {fac(i)}")

n = int(input("Enter a number: "))
print(fac(n))

############################################################

def factorial(n):
    result = 1

    if n > 1:
        for i in range(2, n + 1):
            result *= i

    return result

def factorial2(n):
    result = 1

    if n > 1:
        for _ in range(n):
            result *= n
            n -= 1

    return result

print(factorial(5))
print(factorial2(5))

# Ismétlés nélküli kombináció: n! / k!(n-k)!
print("Hatos: ", factorial2(45) / (factorial2(6) * factorial2(45-6)))
print("Ötös: ", factorial2(90) / (factorial2(5) * factorial2(90-5)))
print("Skandi: ", factorial2(35) / (factorial2(7) * factorial2(35-7)))

def print_fact(n, k):
    print(factorial2(n) / (factorial2(k) * factorial2(n-k)))

n, k = 8, 7
print_fact(n, k)

n, k = 9, 7
print_fact(n, k)

n, k = 10, 7
print_fact(n, k)

n, k = 15, 7
print_fact(n, k)

n, k = 35, 7
print_fact(n, k)

n, k = 45, 6
print_fact(n, k)

print(factorial2(15))
print(factorial2(7))
print(factorial2(8))
print(factorial2(35))

# 
# Ismétlés nélküli variáció
# n! / (n-k)!