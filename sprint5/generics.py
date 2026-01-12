from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    children: List["Person"]
    age:int

fatma = Person(name="Fatma", age=6,children=[])
aisha = Person(name="Aisha", age=10,children=[])

imran = Person(name="Imran", age=40,children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)