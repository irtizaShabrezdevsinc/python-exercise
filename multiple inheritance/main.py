class base:
    var_base = 10

    def __init__(self, name, age):
        print("base con is callled")
        self.name = name
        self.age = age

    def print_detailes(self):
        print(f"the name is {self.name} and the age is {self.age}")


class base_1:
    var_base_1 = 20
    section = "B"
    # def __init__(self, section):
    #     print("base one con is called")
    #     self.section = section

    def print_details(self):
        print(f"section is {self.section}")


class derived(base, base_1):
    var_second_floor = 30

    # def __init__(self, name, age,  section, room_number):
    #     super().__init__()
    #     self.age =
    #     self.room_number = room_number
    #     print("derived con is called")


# "irtiz", 22, "Section B", "204"
var = derived("irtiza", 22)
var.print_details()

