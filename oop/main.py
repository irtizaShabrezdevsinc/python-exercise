# class decorator at 52

class student:
    no_of_leaves = 8  # class attibutes

    def __init__(self, name, age, section):  # self refers to the instance
        self.name = name
        self.age = age
        self.section = section

    @classmethod
    def changes_leaves(cls, leaves):  # refers to the class to change the num of leaves
        cls.no_of_leaves = leaves

    @classmethod
    def from_dash(cls, string):
        temp = string.split("-")
        return cls(temp[0], temp[1], temp[2])

    @staticmethod
    def testing_static(var1, var2):
        # print(name)
        print(var1, var2)

class drived:

# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
st1 = student("test1", 21, "B")
st2 = student("test2", 22, "A")
st1.changes_leaves(10)
print(st2.no_of_leaves)
st3 = student.from_dash("test2-20-A")
print(st3.name)
st1.testing_static("df", "123")
