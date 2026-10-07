from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    children: List["Person"]
    age: int  

fatma = Person(name="Fatma", children=[], age=10)  
aisha = Person(name="Aisha", children=[], age=8)  

imran = Person(name="Imran", children=[fatma, aisha], age=35)

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)

# Fix the above code so that it works. You must not change the print on line 17 - we do want to print the children’s ages.
#  (Feel free to invent the ages of Imran’s children.)