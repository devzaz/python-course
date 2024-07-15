
class Employee():

    raise_amount = 1.05
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@mail.com".format(first, last)

        Employee.num_of_employees += 1

    def fullName(self):
        return "{} {}".format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)


    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}-{}-{}".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return self.pay + other.pay


class Developer(Employee):
    raise_amount = 1.90

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->>",emp.fullName())




dev_1 = Developer("zubaer", 'jisan', 50000, "python")
dev_2 = Developer('test', 'user', 60000, "java")

mng_1 =Manager('test', 'manager', 60000, [dev_1])


emp_1 = Employee("zubaer", 'jisan', 50000)
emp_2 = Employee('test', 'user', 60000, )

print(emp_1.__add__(emp_2))



