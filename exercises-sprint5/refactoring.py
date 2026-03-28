#✍️exercise
#Try changing the type annotation of Person.preferred_operating_system from str to List[str].
#Run mypy on the code.
#It tells us different places that our code is now wrong, because we’re passing values of the wrong type.
#We probably also want to rename our field - lists are plural. Rename the field to preferred_operating_systems.
#Run mypy again.
#Fix all of the places that mypy tells you need changing. Make sure the program works as you’d expect.

from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: List[str]


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
        if laptop.operating_system in person.preferred_operating_systems:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")



# Original code had: preferred_operating_system: str
# Changed to: preferred_operating_systems: List[str]
#
# When I ran mypy after the change, it found 3 errors:
# 1. Line 23: Function was using old field name (preferred_operating_system)
# 2. Line 29: Creating Imran with old field name and string instead of list
# 3. Line 30: Creating Eliza with old field name and string instead of list
#
# Fixes needed:
# - Rename the field everywhere
# - Change == to 'in' (because now it's a list)
# - Change strings to lists: "Ubuntu" → ["Ubuntu"]
#
# The point: mypy acts as a safety net when refactoring.
# It tells you exactly where to update your code.