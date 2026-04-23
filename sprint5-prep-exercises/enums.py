from dataclasses import dataclass
from enum import Enum
import sys
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


def parse_age(raw_age: str) -> int:
    age = int(raw_age)
    if age <= 0:
        raise ValueError("Age must be a positive integer")
    return age


def parse_operating_system(raw_operating_system: str) -> OperatingSystem:
    normalised_value = raw_operating_system.strip().lower()
    for operating_system in OperatingSystem:
        if normalised_value == operating_system.value.lower() or normalised_value == operating_system.name.lower():
            return operating_system

    valid_values = ", ".join(operating_system.value for operating_system in OperatingSystem)
    raise ValueError(f"Preferred operating system must be one of: {valid_values}")


def create_person_from_input() -> Person:
    name = input("Name: ").strip()
    if not name:
        raise ValueError("Name cannot be empty")

    raw_age = input("Age: ").strip()
    raw_operating_system = input("Preferred operating system (Ubuntu, Arch Linux, macOS): ").strip()

    age = parse_age(raw_age)
    preferred_operating_system = parse_operating_system(raw_operating_system)

    return Person(name=name, age=age, preferred_operating_system=preferred_operating_system)


def count_laptops_for_operating_system(laptops: List[Laptop], operating_system: OperatingSystem) -> int:
    return sum(1 for laptop in laptops if laptop.operating_system == operating_system)


def find_most_available_operating_system(laptops: List[Laptop]) -> OperatingSystem:
    counts = {
        operating_system: count_laptops_for_operating_system(laptops, operating_system)
        for operating_system in OperatingSystem
    }
    return max(counts, key=lambda operating_system: counts[operating_system])

def main() -> None:
    laptops = [
        Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
        Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    ]

    try:
        person = create_person_from_input()
    except ValueError as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)

    possible_laptops = find_possible_laptops(laptops, person)
    preferred_count = len(possible_laptops)
    print(f"The library has {preferred_count} laptop(s) with {person.preferred_operating_system.value}.")

    best_operating_system = find_most_available_operating_system(laptops)
    best_count = count_laptops_for_operating_system(laptops, best_operating_system)

    if best_operating_system != person.preferred_operating_system and best_count > preferred_count:
        print(
            f"If you're willing to accept {best_operating_system.value}, "
            f"you're more likely to get a laptop ({best_count} available)."
        )


if __name__ == "__main__":
    main()
