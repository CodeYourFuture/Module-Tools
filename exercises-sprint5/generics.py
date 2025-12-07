#✍️exercise
#Fix the above code so that it works. You must not change the print on line 17 - we do want to print the children’s ages. (Feel free to invent the ages of Imran’s children.)



from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    children: list["Person"]
    age: int

fatma = Person(name="Fatma", age=7, children=[])
aisha = Person(name="Aisha", age=10, children=[])

imran = Person(name="Imran",age=50, children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)


# When I first ran mypy with `children: list`, it found no errors.
# This is because mypy didn't know what type of items were in the list.
# After changing to `children: List["Person"]` (using generics), 
# mypy could identify that each child is a Person object.
# Now it caught the bug: Person has no "age" attribute.
# I fixed this by adding `age: int` to the Person class.