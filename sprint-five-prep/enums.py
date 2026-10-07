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


laptops: List[Laptop] = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


def parse_os(user_input: str) -> OperatingSystem:
    for os in OperatingSystem:
        if os.value.lower() == user_input.lower():
            return os
    raise ValueError("Invalid operating system")


def count_laptops(os: OperatingSystem) -> int:
    return sum(1 for laptop in laptops if laptop.operating_system == os)



def most_available_os() -> OperatingSystem:
    return max(OperatingSystem, key=lambda os: count_laptops(os))



# Main program

name = input("Enter your name: ").strip()

age = None
preferred_os = None

while age is None or preferred_os is None:
    try:
        if age is None:
            age_input = input("Enter your age: ").strip()
            age = int(age_input)
            if age < 0:
                raise ValueError("Age must be a positive number")

        if preferred_os is None:
            os_input = input("Enter OS (macOS, Arch Linux, Ubuntu): ").strip()
            preferred_os = parse_os(os_input)

    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")

        # Reset only the field that failed
        if "Age" in str(e) or "positive number" in str(e):
            age = None
        elif "Invalid operating system" in str(e):
            preferred_os = None


person = Person(name, age, preferred_os)

available = count_laptops(person.preferred_operating_system)
print(f"\nWe have {available} laptops with {person.preferred_operating_system.value}.")

best = most_available_os()
if best != person.preferred_operating_system:
    more = count_laptops(best)
    print(f"If you're flexible, {best.value} has more laptops available ({more}).")



# ✍️exercise
# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input 
# function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user 
# that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more
# constrained types as quickly as possible, and should output errors to stderr and terminate 
# the program with a non-zero exit code if the user input bad values.