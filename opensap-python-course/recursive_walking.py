"""
List generator function: generate an x * y matrix
recursive print function: walk through a matrix and print all elements
"""

def list_generator(x_val = 10, y_val = 10):
    """List generator for x * y"""
    return [x * y for x in list(range(1, x_val+1)) for y in list(range(1, y_val+1))]


def recursive_print(_list, ind = 1):
    """Recursive walking"""
    if _list != []:
        head, *tail = _list
        print(f"{head:3}", end=" ")
        if ind == 20:
            print()
            ind = 0
        recursive_print(tail, ind + 1)


generated_list = [x * y for x in list(range(1, 21)) for y in list(range(1, 21))]
recursive_print(generated_list, 1)

print()

recursive_print(list_generator(20, 20))
print()
recursive_print(list_generator())
