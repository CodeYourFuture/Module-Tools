class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)

# Save the above code to a file, and run it through mypy.

#Read the error, and make sure you understand what it’s telling you.

# The error message simply says that the class: Person does not have "address" as an attribute.
# Therefore, the instances of the class: Person can not inheret an attribute that does not exist.