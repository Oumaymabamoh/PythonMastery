# DRY concept
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal: parent, base
# Mammal: child, sub
class Mammal(Animal):
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


class Fish:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
print(isinstance(m, object))
print(issubclass(Mammal, object))


# multiple inheritance

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
