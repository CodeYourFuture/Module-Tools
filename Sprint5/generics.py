from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age : int
    children: list["Person"] #nside the Person class- the Person-type doesnt exist, so we add "" to person,



Muhib = Person(name="Muhib",age= 7, children=[])
Muiz = Person(name="Muiz",age= 4,children=[])

Sara = Person(name="Sara",age= 31, children=[Muhib, Muiz])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f" {child.name} ({child.age})")

print_family_tree(Sara)