def number_of_digits(n):
    return len(str(n))

def digits(n):
    numstr = []
    n = str(n)
    for index in n:
        numstr.append(int(index))
    return numstr

def isnarcisstic(digits_of_num, number_of_orig_number, orig_number):
    squares = []
    for actual_number in digits_of_num:
        squares.append(actual_number ** number_of_orig_number)
    return sum(squares) == orig_number

numbers_1000 = [(x, isnarcisstic(digits(x), number_of_digits(x), x)) for x in range(1, 1001)]

for i in numbers_1000:
    if i[1] is True:
        print(f"{i[0]} is a narcisstic number.")
