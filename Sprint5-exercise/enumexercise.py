from dataclasses import dataclass
from typing import List
from enum import Enum
import sys


class OperatingSystem(Enum):
    MACOS = "makOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: int
    operating_system: OperatingSystem


@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


def parse_age(age_txt: str) -> int:
    try:
        age = int(age_txt)
    except ValueError:
        print("Error:age must be a valid integer", file=sys.stderr)
        sys.exit(1)

    if age < 0:
        print("Error: age should be a positive number", file=sys.stderr)
        sys.exit(1)

    return age


def parse_operating_system(op_tx: str) -> OperatingSystem:
    normalized = op_tx.strip().lower()

    mapping = {
        "makos": OperatingSystem.MACOS,
        "ubuntu": OperatingSystem.UBUNTU,
        "arch": OperatingSystem.ARCH,
        "arch linux": OperatingSystem.ARCH,
    }

    op: OperatingSystem = mapping.get(normalized)

    if op is None:
        print(
            "Error: operating system must be one of: Ubuntu, Arch Linux, macOS.",
            file=sys.stderr,
        )
        sys.exit(1)

    return op


def find_matching_laptops(
    laptops: List[Laptop], operating_system: OperatingSystem
) -> int:
    counter: int = 0
    for laptop in laptops:
        if laptop.operating_system == operating_system:
            counter += 1

    return counter


def find_most_available(laptops: List[Laptop]) -> OperatingSystem:
    count = {}
    for laptop in laptops:
        if laptop.operating_system in count:
            count[laptop.operating_system] += 1
        else:
            count[laptop.operating_system] = 1
    return max(count, key=count.get)


def main() -> None:

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

    name = input("Enter your name: ").strip()
    if name == "":
        print("Error: name must not be empty", file=sys.stderr)
        sys.exit(1)
    age_txt = input("Enter your age: ")
    operating_system_txt = input("Enter operating system: ")

    age = parse_age(age_txt)
    operating_system = parse_operating_system(operating_system_txt)

    person = Person(
        name=name,
        age=age,
        preferred_operating_system=operating_system,
    )

    matching_laptops_count = find_matching_laptops(
        laptops, person.preferred_operating_system
    )
    print(
        f"Library has {matching_laptops_count} laptop(s) with {person.preferred_operating_system}"
    )

    most_available_os = find_most_available(laptops)

    if most_available_os != person.preferred_operating_system:
        count_most_available_os = find_matching_laptops(laptops, most_available_os)
        print(
            f"If you're willing to accept {most_available_os.value}, "
            f"you're more likely to get a laptop because the library has "
            f"{count_most_available_os} with that operating system."
        )

if __name__ == "__main__":
   main()
