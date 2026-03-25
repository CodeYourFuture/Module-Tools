# ------------------------
# Q. Read the error, and make sure you understand what it’s telling you.
# ------------------------

class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address)

# A. The error is telling me that the 'address' attribute cannot be accessed because it does not exist on the 'Person' class


def is_adult(person: Person) -> bool:
    return person.age >= 18


print(is_adult(imran))


# ------------------------
# Q. Write a new function in the file that accepts a Person as a parameter and tries to access a property that doesn’t exist. Run it through mypy and check that it does report an error.
# ------------------------

# def get_address(person: Person) -> str:
#     return person.address

# A. As in the previous example, the attribute cannot be accessed because it does not exist on the 'Person' class
