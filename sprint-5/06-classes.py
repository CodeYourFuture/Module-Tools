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

# TASK 6.1:
# Run mypy and fix any errors.

# TASK 6.2:
# Create a new function in this file called likes_apple
# It should take a person as parameter
# It returns true if the preferred operating system is "macOS" or "iOS"
# It should return false for any other preferred os
# Add all the appropriate type annotations and test it has no errors in mypy

# TASK 6.3:
# Compare objects and classes
# What are some advantages and disadvantages of each?
