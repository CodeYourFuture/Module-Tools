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

# Answer
# The error returned after running mypy classes_and_objects_exercise1.py means that the Person class does not have an address attribute.
# An instance of Person was created with name, age and preferred_operating_system only.
