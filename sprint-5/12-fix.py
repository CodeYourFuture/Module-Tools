from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Animal:
    name: str
    size: str

@dataclass(frozen=True)
class Person:
    name: str
    age: int

@dataclass(frozen=True)
class Tree[T]:
    parent: T
    children: List[T]

    def print_tree(self):
        print(self.parent)
        for child in self.children:
            print(child)

fatma = Person(name="Fatma", age=4)
aisha = Person(name="Aisha", age=6)
imran = Person(name="Imran", age=30)
family_tree = Tree[Person](parent=imran, children=[fatma, aisha])

cats = Animal(name="Cat", size="Small")
dogs = Animal(name="Dog", size="Medium")
mammals = Animal(name="Mammals", size="Variable")
species_tree = Tree[Animal](parent=mammals, children=[cats, dogs])

family_tree.print_tree()
species_tree.print_tree()

# TASK 12:
# We are going to improve the printing in the above code, you can find a copy in `12-fix.py`.
#
# Experiment with mypy and make sure that the family tree only takes `Person` types and the species tree only takes `Animal` types.
#
# Currently the `Tree.print_tree()` method doesn't look very pretty.
#
# Change only the Animal and Person classes to allow the `Tree.print_tree()` method to display an output that looks like this:
#
# ```
# Imran (30 years old)
# - Fatma (4 years old)
# - Aisha (6 years old))
# Mammals (Variable size)
# - Cat (Small size)
# - Dog (Medium size)
# ```

# STRETCH TASK 12.2
#
# Think of another type of data that can be organised into a tree.
#
# Add a new class for this, instantiate some variables, and have the existing `Tree` class print it out.
