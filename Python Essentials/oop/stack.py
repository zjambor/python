class Stack:

    def __init__(self):
        self.__stack_list = []
        print("Your stack is ready. Use pop and push methods to store or remove objects.")

    def pop(self):
        if len(self.__stack_list) > 0:
            elem = self.__stack_list[-1]
            del self.__stack_list[-1]
            return elem
        else:
            print("The stack is empty.")

    def push(self, obj):
        self.__stack_list.append(obj)

    def print_stack(self):
        r_list = reversed(self.__stack_list)
        for elem in r_list:
            print("[" + str(elem) + "]")

class AddingStack(Stack):

    def __init__(self):
        super().__init__()
        self.__sum = 0

    def get_sum(self):
        return self.__sum

class CountingStack(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        elem = Stack.pop(self)
        self.__counter += 1
        return elem
	

if __name__ == "__main__":
    mystack = Stack()
    mystack.push("Alabama")
    mystack.push("Andorra")
    mystack.print_stack()
    first_stack_elem = mystack.pop()
    print("Elem popped: " + str(first_stack_elem))
    mystack.print_stack()

    myaddingstack = AddingStack()
    myaddingstack.push("Alabama")
    myaddingstack.push("Andorra")
    myaddingstack.print_stack()
    first_stack_elem = myaddingstack.pop()
    print("Elem popped: " + str(first_stack_elem))
    myaddingstack.print_stack()

    stk = CountingStack()
    for i in range(100):
        stk.push(i)
        stk.pop()
    print(stk.get_counter())
