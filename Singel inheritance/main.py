class base:
    def __init__(self):
        print("base con is called")

    def add_numer(self, num1):
        self.num += num1


class derived(base):
    def __init__(self):
        super().__init__()
        self.num = None
        print("derived con is called")

    def minus_number(self, num):
        self.num -= num


var = derived()
var.num = 10
var.add_numer(10)
print(var.num)
var.minus_number(10)
print(var.num)
