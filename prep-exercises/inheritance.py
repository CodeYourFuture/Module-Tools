class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Rex")
cat = Cat("Milo")

print(dog.name, dog.speak())
print(cat.name, cat.speak())