
#EXERCISE 1: Fix the above code so that it works. You must not change the print on line 17 
# we do want to print the children’s ages. (Feel free to invent the ages of Imran’s children)

# SOLUTION:

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int = 0
    children: List["Person"]

fatma = Person(name="Fatma", age=18, children=[])
aisha = Person(name="Aisha", age=24, children=[])

imran = Person(name="Imran", age=45, children=[fatma aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)