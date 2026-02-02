from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: List["Person"]

fatma = Person(name="Fatma", age= 22, children=[])
aisha = Person(name="Aisha", age =21, children=[])

imran = Person(name="Imran", age = 33, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(f"- {person.name} ({person.age})")
    for child in person.children:
        print_family_tree(child)

print_family_tree(imran)
