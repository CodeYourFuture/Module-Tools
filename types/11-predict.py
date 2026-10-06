from dataclasses import dataclass

@dataclass(frozen=True)
class Animal:
    name: str
    species: str

@dataclass(frozen=True)
class Person:
    name: str
    age: int

@dataclass(frozen=True)
class FamilyTree:
    parent: Person
    members: list

pet = Animal(name="Gromit", species="Dog")
fatma = Person(name="Fatma", age=4)
aisha = Person(name="Aisha", age=6)
imran = Person(name="Imran", age=30)

family = FamilyTree(parent=imran, members=[fatma, aisha]) # remove pet here

def print_family_tree(family: FamilyTree):
    print(family.parent.name)
    for child in family.members:
        print(f"{child.name} ({child.age} years old)")

print_family_tree(family)

# TASK 11
# There is a bug in this code. Can you spot it?
# Run your code through mypy. Does mypy spot it?
# Offer an explanation for what is happening.

# Something that gets the gist of:
# The list isn't defined to take a specific type, and the pet was included in it
# When the free function looks at the members list of the family, nothing checked that they were Person types
# Trying to access a non-existent property/attribute caused an AttributeError
# The family tree members list should only contain Person instances