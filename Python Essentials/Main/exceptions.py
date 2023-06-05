try:
    import math
    import time
    import abracadabra
 
except:
    print('One of your imports has failed.')

dictionary = {'a': 'b', 'b': 'c', 'c': 'd'}
ch = 'a'
 
try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)

def read_int(prompt, min, max):
    n = input(prompt)
    while True:
        try:
            n = int(n)
            if n < min or n > max:
                raise Exception
            break
        except ValueError:
            print("Error: wrong input")
            n = input(prompt)
        except:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
            n = input(prompt)
    return n


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)