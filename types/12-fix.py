from dataclasses import dataclass

@dataclass(frozen=True)
class Animal:
    name: str
    size: str

    def __str__(self):
        return f"{self.name} ({self.size} size)"

@dataclass(frozen=True)
class Person:
    name: str
    age: int

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

@dataclass(frozen=True)
class Tree[T]:
    parent: T
    children: list[T]

    def print_tree(self):
        print(self.parent)
        for child in self.children:
            print(f"- {child}") # They must make sure the children are indented
    
    # They do NOT need to make it recursive, but if they do, praise it in your feedback

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
# We are going to improve the printing in the above code.
#
# Experiment with mypy and make sure that the family tree only takes `Person` types and the species tree only takes `Animal` types.
#
# Currently the `Tree.print_tree()` method doesn't look very pretty.
#
# Update the code, adding `__str__()` methods in Animal and Person to allow the `Tree.print_tree()` method to display an output that looks like this:
#
# ```
# Imran (30 years old)
# - Fatma (4 years old)
# - Aisha (6 years old)
# Mammals (Variable size)
# - Cat (Small size)
# - Dog (Medium size)
# ```

# STRETCH TASK 12.2
#
# Think of another type of data that can be organised into a tree.
#
# Add a new class for this, instantiate some variables, and have the existing `Tree` class print it out.

# Any suitable tree-able structure is fine

@dataclass(frozen=True)
class Employee:
    name: str
    pay: str

    def __str__(self):
        return f"{self.name} - annual salary £{self.pay}"
    
ceo = Employee(name="CEO", pay=100000)
hr_admin = Employee(name="HR Administrator", pay=40000)
salesperson = Employee(name="Sales Person", pay=30000)
job_tree = Tree[Employee](parent=ceo, children=[hr_admin, salesperson])

job_tree.print_tree()
