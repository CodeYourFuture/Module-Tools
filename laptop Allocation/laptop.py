from dataclasses import dataclass
from enum import Enum
from typing import Dict, List
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_systems: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

#library of laptops
laptop = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Dell", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=7, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=8, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]
# Preset dataset of people
people = [
    Person(name="Sara", age=31, preferred_operating_system=[OperatingSystem.ARCH,OperatingSystem.UBUNTU]),
    Person(name="Shabs", age=40, preferred_operating_system=[OperatingSystem.ARCH,OperatingSystem.MACOS,OperatingSystem.UBUNTU]),
    Person(name="Jawad", age= 36, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.UBUNTU,OperatingSystem.ARCH]),    
    Person(name="Mike", age=35, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.ARCH]),
    Person(name="Mawra", age=28, preferred_operating_system=[OperatingSystem.MACOS]),
    Person(name="Fatma", age= 22, preferred_operating_system=[OperatingSystem.UBUNTU,OperatingSystem.ARCH]),    
    Person(name="Muhib", age= 19, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.UBUNTU]),    

]

def sadness(person: Person, laptop: Laptop) -> int:
    if laptop.operating_system == person.preferred_operating_systems[0]:
        return 0
    elif len(person.preferred_operating_systems) > 1 and laptop.operating_system == person.preferred_operating_systems[1]:
        return 1
    elif len(person.preferred_operating_systems) > 2 and laptop.operating_system == person.preferred_operating_systems[2]:
        return 2
    else:
        return 100
    
#There are two approaches to solve this
#Greedy approach or Hungarian Algorithm Approach

#def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
