from dataclasses import dataclass
from enum import Enum
from typing import List
import sys

class OperatingSystem(Enum):
    MACOS = "macos"
    ARCH = "arch linux"
    UBUNTU = "ubuntu"

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


people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

name = input("Please enter your name: ")

def get_age() -> int:
    while True:
        try:
            age_string = input("Please enter your age, you must be >= 18 years old: ")
            age = int(age_string)

            if age < 18:
                print("You must be 18+.")
                continue

            return age
        except ValueError:
            print("Please enter a valid number.")

age = get_age()

def get_preferred_operating_system() -> OperatingSystem:
    while True:
        preferred_operating_system_input = input("Your preferred operating system (macOS, Ubuntu or Arch Linux): ")

        try:
            normalised_value = preferred_operating_system_input.strip().lower()
            operating_system = OperatingSystem(normalised_value)
            return operating_system
        except ValueError:
            print(f"Sorry, we don't have {preferred_operating_system_input}. Please choose from macOS, Ubuntu or Arch Linux.")

operating_system = get_preferred_operating_system()

person = Person(name=name, age=age, preferred_operating_system=operating_system)
people.append(person)

def find_laptop() -> None:
    matching_laptops = []
    non_matching_laptops = []

    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            matching_laptops.append(laptop)
        else:
            non_matching_laptops.append(laptop)

    if matching_laptops:
            count = len(matching_laptops)
            print(f"Congratulations, we have found {count} matching laptops!")

            other_laptops_count = len(non_matching_laptops)
            
            if other_laptops_count > count:
                print(f"We have found {other_laptops_count} laptops with other operating systems. You might be interested in switching to a different operating system.")
            
            sys.exit(0)
    else:
        sys.exit("Sorry, we couldn't find any matching laptops!")
        

find_laptop()
