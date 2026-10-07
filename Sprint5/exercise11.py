#Write a program which:

#Already has a list of Laptops that a library has to lend out.
#Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
#Tells the user how many laptops the library has that have that operating system.
#If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
#You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

from dataclasses import dataclass
from enum import Enum
from typing import List
import sys


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(
    laptops: List[Laptop],
    person: Person
) -> List[Laptop]:
    possible_laptops = []

    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)

    return possible_laptops


laptops = [
    Laptop(
        id=1,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
    Laptop(
        id=2,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=3,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=15,
        operating_system=OperatingSystem.UBUNTU,
    ),
    Laptop(
        id=4,
        manufacturer="Apple",
        model="MacBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


name = input("What is your name? ")

try:
    age = int(input("What is your age? "))
except ValueError:
    print("Error: age must be a number.", file=sys.stderr)
    sys.exit(1)


print("Available operating systems:")
for operating_system in OperatingSystem:
    print(f"- {operating_system.value}")

preferred_os_input = input("What is your preferred operating system? ")

try:
    preferred_operating_system = OperatingSystem(preferred_os_input)
except ValueError:
    print(
        f"Error: '{preferred_os_input}' is not a valid operating system.",
        file=sys.stderr,
    )
    sys.exit(1)


person = Person(
    name=name,
    age=age,
    preferred_operating_system=preferred_operating_system,
)


possible_laptops = find_possible_laptops(laptops, person)

print(
    f"The library has {len(possible_laptops)} "
    f"laptop(s) with {person.preferred_operating_system.value}."
)


laptop_counts = {}

for laptop in laptops:
    laptop_counts[laptop.operating_system] = (
        laptop_counts.get(laptop.operating_system, 0) + 1
    )

most_available_os = max(
    laptop_counts,
    key=laptop_counts.get
)


if (
    most_available_os != person.preferred_operating_system
    and laptop_counts[most_available_os] > len(possible_laptops)
):
    print(
        f"There are more {most_available_os.value} laptops available. "
        f"If you're willing to accept {most_available_os.value}, "
        f"you're more likely to get a laptop."
    )