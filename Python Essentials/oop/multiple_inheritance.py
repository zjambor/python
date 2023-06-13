class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB):
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

# Override

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub1(Left, Right):
    pass


obj = Sub1()

print(obj.var, obj.var_left, obj.var_right, obj.fun())


# Method Resolution Order (MRO)

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")


# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
# class Bottom(Top, Middle):
#     def m_bottom(self):
#         print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
