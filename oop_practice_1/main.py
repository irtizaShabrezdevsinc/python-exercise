class base:
    all = []

    def __init__(self, name: str, age):
        # print("parameterized con called")
        # Run validation to the receive arguments
        assert age >= 18, f"Age {age} lower then 18"
        # print(f"my name is {name}")
        self.name = name
        self.age = age
        base.all.append(self)

    def get_age(self):
        return self.age
    def __repr__(self):
        return f"Info('{self.name}, {self.age}'"

print("============================================")

a = base("irtiza", 18)
a = base("irtisdf4za", 168)

print(a.name, a.age)
print(a.get_age())
print(base.all)
