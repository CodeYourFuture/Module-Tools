from enum import Enum
from dataclasses import dataclass
import sys


# Enum gives us a fixed set of operating system choices.
class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


# Dataclass automatically creates the __init__ method for us.
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


# The laptops already available in the library.
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
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
]


# Get the user's name.
name = input("What is your name? ")


# Convert the age from a string to an integer.
# If conversion fails, print the error to stderr and exit with code 1.
try:
    age = int(input("What is your age? "))
except ValueError:
    print("Invalid age.", file=sys.stderr)
    sys.exit(1)


# Convert the user's input into an OperatingSystem enum value.
# If the input is invalid, ask the user to try again.
while True:
    try:
        preferred_operating_system = OperatingSystem(
            input(
                "What is your preferred operating system "
                "(macOS, Arch Linux, or Ubuntu)? "
            )
        )
        break
    except ValueError:
        print(
            "Invalid operating system. " "Please choose macOS, Arch Linux, or Ubuntu."
        )


# Create a Person using the validated input.
person = Person(
    name=name,
    age=age,
    preferred_operating_system=preferred_operating_system,
)


# Count laptops matching the person's preferred operating system.
count = 0

for laptop in laptops:
    if laptop.operating_system == person.preferred_operating_system:
        count += 1


print(
    f"There are {count} laptops available with "
    f"{person.preferred_operating_system.value}."
)


# Count how many laptops are available for each operating system.
available_laptops = {}

for laptop in laptops:
    os = laptop.operating_system

    if os not in available_laptops:
        available_laptops[os] = 0

    available_laptops[os] += 1


# Find the operating system with the most available laptops.
most_available_os = max(
    available_laptops,
    key=available_laptops.__getitem__,
)


# If another operating system has more laptops, recommend it.
if most_available_os != person.preferred_operating_system:
    print(
        f"You are more likely to get a laptop if you accept "
        f"{most_available_os.value}."
    )


# # LAPTOP LIBRARY PROGRAM FLOW:
#
# 1. Define OperatingSystem enum
#       ↓
# 2. Define Person and Laptop dataclasses
#       ↓
# 3. Create list of available laptops
#       ↓
# 4. Get user's name, age, and preferred OS
#       ↓
# 5. Validate and convert user input
#       ↓
# 6. Create a Person object
#       ↓
# 7. Count laptops matching the user's preferred OS
#       ↓
# 8. Count laptops for each operating system
#       ↓
# 9. Find the OS with the most laptops
#       ↓
# 10. Compare it with the user's preferred OS
#       ↓
# 11. Recommend another OS if more laptops are available
