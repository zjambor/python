def dupla_fakt(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return dupla_fakt(n - 2) * n

n = int(input("Enter a number: "))
print("Dupla fakt:", dupla_fakt(n))

input("Press enter to exit;")
