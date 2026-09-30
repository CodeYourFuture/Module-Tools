from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: str


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_system="ubuntu"),
    Person(name="Eliza", age=34, preferred_operating_system="arch"),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="arch"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macos"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")

# TASK 14
# The above code currently handles operating systems as strings.
#
# Refactor the code to use enums for operating systems.
#
# Check with mypy and test it to ensure the program still works correctly.
#
# Replace the list of existing people with the `input` function
# https://docs.python.org/3/library/functions.html#input
# to read a person's name, age, and preferred operating system.
#
# Make sure your implementation has a good user experience, and properly validates the inputs, mapping an OS to one of the enum values.
#
# If an operating system can't be matched at all, your script should handle it appropriately and not crash.
