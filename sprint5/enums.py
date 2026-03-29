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

def get_name() -> str:
    while True:
        name = input("Name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")

def get_age() -> int:
    while True:
        age_input = input("Age: ").strip()
        try:
            age=int(age_input)
            if age>0:
                return age
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("Age must be a number.")                
def get_os() -> OperatingSystem:
    os_values = [os.value for os in OperatingSystem]
    while True:
        os_input = input(f"Preferred OS ({', '.join(os_values)}): ").strip()
        try:
            return OperatingSystem(os_input)
        except ValueError:
            print(f"'{os_input}' is not a valid operating system. Please try again.")
            
name=get_name()
age=get_age()
preferred_os=get_os()

person = Person(name=name, age=age, preferred_operating_system=preferred_os)

def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    return [laptop for laptop in laptops if laptop.operating_system == person.preferred_operating_system]

possible_laptops = find_possible_laptops(laptops, person)
print(f"There are {len(possible_laptops)} laptops matching your preferred OS ({person.preferred_operating_system.value}).")

other_counts = {os: sum(1 for l in laptops if l.operating_system == os) for os in OperatingSystem}
most_available_os = max(other_counts, key=other_counts.get)

if most_available_os != person.preferred_operating_system and other_counts[most_available_os] > len(possible_laptops):
    print(f"If you are willing to accept {most_available_os.value}, there are more laptops available ({other_counts[most_available_os]}).")