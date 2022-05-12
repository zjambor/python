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