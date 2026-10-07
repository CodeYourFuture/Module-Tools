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


name = input("What is your name? ")

try:
    age = int(input("What is your age? "))
except ValueError:
    print("Age must be a number.", file=sys.stderr)
    sys.exit(1)


print("Available operating systems:")
for os in OperatingSystem:
    print(os.value)

try:
    os_input = input("What is your preferred operating system? ").strip().lower()

    operating_system = next(
        os for os in OperatingSystem
        if os.value.lower() == os_input
    )

except StopIteration:
    print("Invalid operating system.", file=sys.stderr)
    sys.exit(1)


person = Person(
    name=name,
    age=age,
    preferred_operating_system=operating_system,
)


number_available = sum(
    laptop.operating_system == person.preferred_operating_system
    for laptop in laptops
)

print(
    f"We have {number_available} laptop(s) with "
    f"{person.preferred_operating_system.value}."
)


counts: dict[OperatingSystem, int] = {}

for os in OperatingSystem:
    counts[os] = sum(
        laptop.operating_system == os
        for laptop in laptops
    )


most_available_os = max(counts, key=counts.get)

if most_available_os != person.preferred_operating_system:
    if counts[most_available_os] > number_available:
        print(
            f"If you are willing to use {most_available_os.value}, "
            f"you are more likely to get a laptop because we have "
            f"{counts[most_available_os]} available."
        )