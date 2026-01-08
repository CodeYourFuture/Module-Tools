from dataclasses import dataclass
from enum import Enum
from typing import List
import sys
from collections import Counter


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


name = input("Insert your name :")
if len(name) == 0:
    print("Name cannot be empty!", file=sys.stderr)
    exit(1)
elif len(name) > 50:
    print("Name is too long!", file=sys.stderr)
    exit(1)
try:
    age = int(input("Insert your age :"))
    if age < 18 or age > 100:
        raise ValueError("Age out of range")
except ValueError as e:
    print(f"Invalid age: {e}", file=sys.stderr)
    sys.exit(1)
preferred_os = input(
    "Insert your preferred_operating_system(macOS,Arch Linux,Ubuntu) :"
)
try:
    preferred_operating_system = OperatingSystem(preferred_os)
except ValueError:
    print("error in os name", file=sys.stderr)
    sys.exit(1)

person = Person(name, age, preferred_operating_system)


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
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
        model="macBook",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.MACOS,
    ),
    Laptop(
        id=5,
        manufacturer="Dell",
        model="XPS",
        screen_size_in_inches=13,
        operating_system=OperatingSystem.ARCH,
    ),
]

os_count = Counter(laptop.operating_system for laptop in laptops)
max_count = max(os_count.values())
print(max_count)
most_available_os = []
for os in os_count:
    count = os_count[os]
    if count == max_count:
        most_available_os.append(os.value)
print(most_available_os)
possible_laptops = find_possible_laptops(laptops, person)
print(
    f"Count of available  {person.preferred_operating_system.value} laptops for {person.name} is : {len(possible_laptops)}"
)

if len(possible_laptops) < max_count:
    print(
        f"Note: If you are willing to accept : {" or ".join(most_available_os)}, you are more likely to get a laptop."
    )
