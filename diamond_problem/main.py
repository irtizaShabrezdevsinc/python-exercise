class A:
    def method(self):
        print("This is method from class A")

class B(A):
    def method(self):
        print("This is method from class B")


class C(A):
    # def method(self):
    #     print("This is method from class C")
    pass

class D(B, C):
    def method(self):
        print("This is method from class D")


a = C()
a.method()