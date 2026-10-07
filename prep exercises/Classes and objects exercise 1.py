class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address) # error: "Person" has no attribute "address"  [attr-defined]

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address) # error: "Person" has no attribute "address"  [attr-defined]

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

def no_attribute_exists(person: Person):
    print(person.dob)

# mypy detects that dob attribute doesn't exist.
# error: "Person" has no attribute "dob"  [attr-defined]
