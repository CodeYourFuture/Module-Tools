class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str, address: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.address = address

imran = Person("Imran", 22, "Ubuntu", "London street")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux", "Hatfield town")
print(eliza.name)
print(eliza.address)

# ====function to check if imran is an adult===========
def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))


def address(person: Person) -> str:
    return person.city #city property does not exist

print(address(imran))
