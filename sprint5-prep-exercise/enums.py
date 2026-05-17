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


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops



laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age. Must be number!", file=sys.stderr)
    sys.exit(1)

os_input = input("Enter preferred OS (macOS / Arch Linux / Ubuntu): ")

try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print("Invalid operating system.", file=sys.stderr)
    sys.exit(1)

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

matching = find_possible_laptops(laptops, person)

print(f"\nWe have {len(matching)} laptop(s) with {person.preferred_operating_system.value}.")

# Compare with other OS availability
os_counts = {}

for laptop in laptops:
    os_counts[laptop.operating_system] = os_counts.get(laptop.operating_system, 0) + 1

best_os = max(os_counts, key=os_counts.get)

if best_os != person.preferred_operating_system:
    print(
        f"If you're flexible, {best_os.value} has more laptops available "
        f"({os_counts[best_os]} total)."
    )
