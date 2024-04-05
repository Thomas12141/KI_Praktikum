class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " barks")


class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(self.name + " meows")


animal1 = Dog("Thomas")
animal2 = Cat("Leo")

animals = [animal1, animal2]

for animal in animals:
    match animal:
        case Dog():
            animal.bark()
        case Cat():
            animal.meow()

