from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
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

def user_register() -> Person:

    user_name: str = input("Please enter your name: ")
    user_age_str: str = input("Please enter your age: ")

    try:
        user_age: int = int(user_age_str)
        if user_age < 0:
            raise ValueError
    except ValueError:
        sys.stderr.write(f'Error: "{user_age_str}" is not a valid age. \n')
        sys.exit(1)

    user_system_str = input("Please enter your preferred operating system - Arch Linux, Ubuntu, or macOS: ")

    try:
        user_system = OperatingSystem(user_system_str)
    except ValueError:
        sys.stderr.write(f'Error: "{user_system_str}" is not a valid system. \n')
        sys.exit(1)

    return Person(name=user_name, age=user_age, preferred_operating_system=user_system)


def matching_laptop(new_user: Person = user_register()) -> None:
    possible_laptops = find_possible_laptops(laptops=laptops, person=new_user)

    print(f'Library has {len(possible_laptops)} laptops have {new_user.preferred_operating_system.value}')

    system_counts: Dict[OperatingSystem, int] = {}
    for laptop in laptops:
        system_counts[laptop.operating_system] = (system_counts.get(laptop.operating_system) or 0 ) + 1

    most_available = max(system_counts, key=lambda name: system_counts[name])

    if system_counts[most_available] > len(possible_laptops):
        print(f'if you are willing to accept {most_available.value} you are more likely to get a laptop.')


matching_laptop()
