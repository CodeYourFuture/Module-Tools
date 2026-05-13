class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


def is_adult(person: Person) -> bool:
    return person.age >= 18


imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# there is no property 'address' in Person class
# print(imran.address)
print(is_adult(imran))

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# there is no property 'address' in Person class
# print(eliza.address)
