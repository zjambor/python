
def factorial2(n):
    result = 1

    if n > 1:
        for _ in range(n):
            result *= n
            n -= 1

    return result

n = int(input("Enter a number: "))
print(factorial2(n))

print("Skandi: ", factorial2(35) / (factorial2(7) * factorial2(35-7)))

input("Press enter to exit;")
