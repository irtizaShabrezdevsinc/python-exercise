class base:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"my name is {self.name} and my age is {self.age}")

    def __add__(self, other):
        return self.age + other.age

    def __mod__(self, other):
        return self.age % other.age


var = base("test1", 22)
var2 = base("test2", 21)

print(var % var2)
