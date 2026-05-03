from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int  # Added the missing field
    children: List["Person"]

# Inventing ages for the family members
fatma = Person(name="Fatma", age=8, children=[])
aisha = Person(name="Aisha", age=10, children=[])

# Imran needs an age as well, and now includes his children
imran = Person(name="Imran", age=40, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        # This line now works because 'age' exists in the Person class
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)