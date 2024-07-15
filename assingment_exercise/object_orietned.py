class Employee():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def display(self):
        return "{}- {}".format(self.id, self.name)

emp_1 = Employee(1, "zaz")
print(emp_1.display)
