import sys
from sys import stderr
from dataclasses import dataclass
from enum import Enum
from typing import List

class OperatingSystem(Enum):
    MACOS = "macos"
    ARCH = "arch linux"
    UBUNTU = "ubuntu"

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

available_laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="HP", model="Spectre", screen_size_in_inches=13, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=6, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14, operating_system=OperatingSystem.ARCH),
    Laptop(id=7, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=16, operating_system=OperatingSystem.MACOS),
    Laptop(id=8, manufacturer="Dell", model="Inspiron", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=9, manufacturer="Asus", model="ZenBook", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
]



def error_exit(message: str, code: int =1) -> None:
    print(f"Error: {message}", file=stderr)
    sys.exit(code)

def number_of_laptops_per_os() -> dict[OperatingSystem, int]:
    os_count: dict[OperatingSystem, int] = {
        OperatingSystem.MACOS: 0,
        OperatingSystem.ARCH: 0,
        OperatingSystem.UBUNTU: 0,
    }
    for laptop in available_laptops:
        os_count[laptop.operating_system] += 1
    return os_count

def main() -> None:
    name: str = input("Enter your name: ").strip()
    if not name:
        error_exit("Name cannot be empty.")
    
    try:
        age: int = int(input("Enter your age: ").strip())
        if age <= 0:
            error_exit("Age must be a positive integer.")
    except ValueError:
        error_exit("Invalid age. Please enter a positive integer.")

    try:
        preferred_operating_system: OperatingSystem = OperatingSystem(input("Enter your preferred operating system (macOS, Arch Linux, Ubuntu): ").strip().lower())
    except ValueError:
        error_exit("Invalid operating system. Choose from macOS, Arch Linux, Ubuntu.") 
    
    person = Person(name=name, age=age, preferred_operating_system=preferred_operating_system)
 
    os_count = number_of_laptops_per_os()
    print(f"Hi {person.name}, there are {os_count[preferred_operating_system]} laptops available with {preferred_operating_system.value}.")
    max_os, max_count = max(os_count.items(), key=lambda item: item[1])
    print(f"The operating system with the most laptops is {max_os.value} with {max_count} laptops.")
    print ("person:", person)


if __name__ == "__main__":
    main()