from dataclasses import dataclass
from enum import Enum
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


laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "MacBook", 13, OperatingSystem.MACOS),
]


# Read name
name = input("Enter your name: ")

# Read and convert age
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: age must be a whole number.", file=sys.stderr)
    sys.exit(1)

# Read and convert operating system
print("Choose an operating system:")
print("- Ubuntu")
print("- Arch Linux")
print("- macOS")

while True:
    os_input = input("Preferred operating system: ")

    try:
        preferred_os = OperatingSystem(os_input)
        break
    except ValueError:
        print("Please choose Ubuntu, Arch Linux, or macOS.")

# Create the person
person = Person(name, age, preferred_os)

# Find matching laptops
matching = [
    laptop
    for laptop in laptops
    if laptop.operating_system == person.preferred_operating_system
]

print(
    f"\nThe library has {len(matching)} laptop(s) running "
    f"{person.preferred_operating_system.value}."
)

# Count laptops for each operating system
counts = {}

for laptop in laptops:
    os = laptop.operating_system
    counts[os] = counts.get(os, 0) + 1

best_os = max(counts, key=counts.get)

if best_os != person.preferred_operating_system:
    print(
        f"If you're willing to accept {best_os.value}, "
        f"there are {counts[best_os]} laptops available."
    )