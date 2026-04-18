class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str) -> None:
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


def is_adult(person: Person) -> bool:
    return person.age >= 18


def get_postal_address(person: Person) -> str:
    return person.address


imran = Person("Imran", 22, "Ubuntu")
eliza = Person("Eliza", 34, "Arch Linux")

print(imran.name)
print(eliza.name)
print(is_adult(imran))
print(is_adult(eliza))