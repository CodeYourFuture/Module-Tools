class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


def is_adult(person: Person) -> bool:
    return person.age >= 18


def double(person: Person) -> int:
    return person.price * 2


imran = Person("Imran", 22, "Ubuntu")
print(imran.name)


eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)


print(is_adult(imran))
