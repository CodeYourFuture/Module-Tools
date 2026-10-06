class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str, address: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.address = address # 6.1 possible answer A

imran = Person("Imran", 22, "Ubuntu", "123 High Street") # 6.1 possible answer A
print(imran.name)
# print(imran.address)
print(imran.preferred_operating_system) # 6.1 possible answer B

eliza = Person("Eliza", 34, "Arch Linux", "123 High Street")
print(eliza.name)
# print(eliza.address)
print(eliza.preferred_operating_system) # 6.1 possible answer B

# TASK 6.1:
# Run mypy and fix any errors.
# Either add the missing attribute, or change what is printed

# TASK 6.2:
# Create a new function in this file called likes_apple
# It should take a person as parameter
# It returns true if the preferred operating system is "macOS" or "iOS"
# It should return false for any other preferred os
# Add all the appropriate type annotations and test it has no errors in mypy

def likes_apple(person: Person) -> bool:
    return person.preferred_operating_system in ["macOS", "iOS"]
print(likes_apple(eliza))

print(eliza)
print({
  "name": "Eliza",
  "age": 34,
  "preferred_operating_system": "Arch Linux",
})

# TASK 6.3:
# Compare objects and classes
# What are some advantages and disadvantages of each?

# any of, not limited to:
# Objects are freeform, so are easier to start prototyping with
# Objects format automatically when printed in python, classes need some extra steps
# Classes are strict so the interpeter/compiler/type checker can spot mistakes more easily
# Classes offer more natural semantics and make code easier to read and write
# Well defined classes are more maintainable than objects
# Discussion of more advanced topics covered later in the prep, such as encapsulation, inheritance, etc.