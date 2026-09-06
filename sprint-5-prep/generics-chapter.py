from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    children: list["Person"]

fatma = Person(name="Fatma", children=[], age=5)
aisha = Person(name="Aisha", children=[], age=3)

imran = Person(name="Imran", children=[fatma, aisha], age=35)

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)
