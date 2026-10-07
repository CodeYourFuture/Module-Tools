from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age : int
    children: List["Person"]

france = Person(name="France", age=5, children=[])
aisha = Person(name="Aisha", age= 1, children=[])

amy = Person(name="Amy",age = 32, children=[france, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(amy)