def is_prime(n):
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            print(n, 'is not prime')
            return False

    print(n, 'is prime')
    return True

if __name__ == '__main__':
    is_prime(132211)