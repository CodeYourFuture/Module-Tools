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

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

def count_laptops(laptops: List[Laptop], operating_system: OperatingSystem) -> int:
    count = 0
    for laptop in laptops:
        if laptop.operating_system == operating_system:
            count += 1
    return count

def most_available_os(laptops: List[Laptop]) -> OperatingSystem:
    best_os = OperatingSystem.UBUNTU
    best_count = count_laptops(laptops, best_os)

    for os in OperatingSystem:
        current_count = count_laptops(laptops, os)
        if current_count > best_count:
            best_count = current_count
            best_os = os

    return best_os

name = input("Enter your name: ")
age = int(input("Enter your age: "))
os_input = input("Enter preferred OS (macOS, Arch Linux, Ubuntu):  ")

try:
    preferred_os = OperatingSystem(os_input)
except ValueError:
    print("Invalid operating system.")
    exit()

person = Person(name, age, preferred_os)

available = count_laptops(laptops, person.preferred_operating_system)

print(
    f"\nThere are {available} {person.preferred_operating_system.value} laptop(s) available."
)

best_os = most_available_os(laptops)

if best_os != person.preferred_operating_system:
    print(
        f"If you're willing to accept {best_os.value}, you're more likely to get a laptop."
    )
