class A:
    var_a = "I am a variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A constructor "


class B(A):
    var_b = "I am a variable in class B"

    # def __init__(self):
    #     self.var1 = "I am inside class A constructor "


a = A()
b = B()
print(b.var_b)