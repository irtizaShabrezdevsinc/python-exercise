class base:
    var_base = 10

    def __init__(self):
        print("base con is callled")

    def floor_up(self):
        print("I can go to first floor")

    @classmethod
    def change_base_var(cls, num):
        cls.var_base = num


class first_floor(base):
    var_first_floor = 20

    def __init__(self):
        super().__init__()
        print("first floor con is called")

    def floor_up(self):
        print("I can go to second floor")


class second_floor(first_floor):
    var_second_floor = 30

    def __init__(self):
        super().__init__()
        print("second floor con is called")

    def floor_up(self):
        print("there is no more floor second floor is max")


var1 = first_floor()
# var.change_base_var(99)
# print(var.var_base)
var2 = second_floor()

# print(var1.var_base)
var2.floor_up()

print(var2.var_base)