import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))



print(module.__name__)
zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.__counter)
print(module.suml(zeroes))
print(module.prodl(ones))
print(module.__counter)


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
