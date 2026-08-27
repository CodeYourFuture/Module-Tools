class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.age)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.age)


def is_adult(person: Person) -> bool:
    return person.age >= 18


print(is_adult(imran))


def get_address(person: Person) -> str:
    return person.address
    # it still gives error as Person class does not have any attribute called address.


# this is the error given by mypy:
# class-in-python.py:10: error: "Person" has no attribute "address"  [attr-defined]
# class-in-python.py:14: error: "Person" has no attribute "address"  [attr-defined]
# Found 2 errors in 1 file (checked 1 source file)

# Solution:
# The Person class doesn't define an address attribute, but the code tries to access it. To fix the error, either remove the address references or define address as an attribute in the constructor and provide it when creating each Person object.
