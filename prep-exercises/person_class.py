class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address) - Person class has no address attribute, hence the error message in mypy on lines 9 and 13

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address) - same as line 9

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

# This function will generate an attribute error when mypy runs it, because gender is not an attribute of the class, Person.
def check_gender(person: Person) -> str:
    return person.gender
