class Animal():
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some animal sound")


class Dog(Animal):

    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("woof woof")

x = Dog()

x.print_habitat()
x.sound()

print(isinstance(x, Dog))
