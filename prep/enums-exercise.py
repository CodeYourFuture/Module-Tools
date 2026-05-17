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
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


def create_person_from_input(laptops: List[Laptop]) -> None:
    name = input("Enter person's name: ")
    age = int(input("Enter person's age: "))
    
    print("Available operating systems:")
    for os in OperatingSystem:
        print(f"  {os.name}: {os.value}")
    
    os_choice = input("Enter preferred operating system (MACOS/ARCH/UBUNTU): ").upper()
    
    try:
        preferred_os = OperatingSystem[os_choice]
    except KeyError:
        print("Invalid operating system choice!", file=sys.stderr)
        sys.exit(1)
    
    person = Person(name=name, age=age, preferred_operating_system=preferred_os)
    possible_laptops = find_possible_laptops(laptops, person)
    
    print(f"\nPossible laptops for {person.name}: {possible_laptops}")
    print(f"The library has {len(possible_laptops)} laptop(s) with {preferred_os.value}")

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")

print("\n--- Create a new person ---")
create_person_from_input(laptops)