from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    #Add "age" attribute
    age: int
    children: List["Person"]

#Add "age" field and thier respective values to "fatma" and "aisha" - instances of class "Person"
fatma = Person(name="Fatma", age=14, children=[])
aisha = Person(name="Aisha",age=22, children=[])

##Add "age" field and its values to "imran" -  instance of class "Person"
imran = Person(name="Imran", age=44, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)


#Fix the above code so that it works. You must not change the print on line 17 - we do want to print the
#children’s ages. (Feel free to invent the ages of Imran’s children.)


