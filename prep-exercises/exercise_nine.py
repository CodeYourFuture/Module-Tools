from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    #Add "age" attribute
    age: int
    children: List["Person"]

#Add great grandchildren to the main object imran to demonsrate that function works recursively
jameeela = Person(name="Jameeela", age=10, children=[])
sameera = Person(name="Sameera", age=8, children=[])

#Add a grandchild to the main object imran to demonsrate that function works recursively
khaled = Person(name="Khaled", age=32, children=[jameeela, sameera])

#Add "age" field and thier respective values to "fatma" and "aisha" - instances of class "Person"
fatima = Person(name="Fatma", age=46, children=[])
aisha = Person(name="Aisha",age=53, children=[khaled])

##Add "age" field and its values to "imran" -  instance of class "Person"
imran = Person(name="Imran", age=79, children=[fatima, aisha])

def print_family_tree(person: Person, level: int = 0) -> None:
    indent = " " * level
    print(f"{indent}{person.name} ({person.age})")
    for child in person.children:
        print_family_tree(child, level + 1)

print_family_tree(imran)


#Fix the above code so that it works. You must not change the print on line 17 - we do want to print the
#children’s ages. (Feel free to invent the ages of Imran’s children.)


