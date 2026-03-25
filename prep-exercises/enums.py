# ------------------------
# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.
# ------------------------

# A.

import sys
from dataclasses import dataclass
from enum import Enum
from typing import List


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


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops: List[Laptop] = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS",
           screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS",
           screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS",
           screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook",
           screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

try:
    user_name = input('Enter your name: ')
    if not user_name.strip():
        raise ValueError("Name cannot be empty")
except ValueError:
    sys.stderr.write("Error: Please provide a valid name\n")
    sys.exit(1)

try:
    user_age_input = input('Enter your age: ')
    user_age = int(user_age_input)
    if user_age < 0:
        raise ValueError("Age cannot be negative")
except ValueError:
    sys.stderr.write("Error: Please provide a valid age\n")
    sys.exit(1)

try:
    user_os_input = input(
        'Enter your preferred operating system (macOS, Arch Linux, Ubuntu): ')
    user_os = OperatingSystem(user_os_input)
except ValueError:
    sys.stderr.write("Error: Please enter a valid operating system\n")
    sys.exit(1)

person = Person(name=user_name, age=user_age,
                preferred_operating_system=user_os)

possible_laptops = find_possible_laptops(laptops, person)
print(f"We have {len(possible_laptops)} laptop(s) with {user_os.value}")

# Find OS with most laptops
os_counts: dict[OperatingSystem, int] = {}
for laptop in laptops:
    os_counts[laptop.operating_system] = os_counts.get(
        laptop.operating_system, 0) + 1

best_os = max(os_counts, key=lambda os: os_counts[os])
if best_os != user_os and os_counts[best_os] > len(possible_laptops):
    print(
        f"If you're willing to accept {best_os.value}, you're more likely to get a laptop ({os_counts[best_os]} available)")
