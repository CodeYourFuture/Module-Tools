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

laptops = [
    Laptop(1, "Dell", "XPS", 13, OperatingSystem.ARCH),
    Laptop(2, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(3, "Dell", "XPS", 15, OperatingSystem.UBUNTU),
    Laptop(4, "Apple", "macBook", 13, OperatingSystem.MACOS),
]


name = input("Name: ").strip()
age_input = input("Age: ").strip()
os_input = input("Preferred OS (macOS, Arch Linux, Ubuntu): ").strip()

try:
    age = int(age_input)
except ValueError:
    print("Error: Age must be a number.", file=sys.stderr)
    sys.exit(1)

try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print(f"Error: '{os_input}' is not a valid operating system.", file=sys.stderr)
    sys.exit(1)

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    return [laptop for laptop in laptops if laptop.operating_system == person.preferred_operating_system]

possible_laptops = find_possible_laptops(laptops, person)
print(f"There are {len(possible_laptops)} laptops matching your preferred OS ({person.preferred_operating_system.value}).")

other_counts = {os: sum(1 for l in laptops if l.operating_system == os) for os in OperatingSystem}
most_available_os = max(other_counts, key=other_counts.get)

if most_available_os != person.preferred_operating_system and other_counts[most_available_os] > len(possible_laptops):
    print(f"If you are willing to accept {most_available_os.value}, there are more laptops available ({other_counts[most_available_os]}).")
