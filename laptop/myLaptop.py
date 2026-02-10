from dataclasses import dataclass
from enum import Enum
from typing import List

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
    WINDOWS = "Windows"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: List[OperatingSystem]

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def allocate_laptops(
    people: List[Person],
    laptops: List[Laptop]
) -> dict[str, tuple[str, int]]:

    allocation_map = {}
    available_laptops = laptops.copy()

    if len(laptops) < len(people):
        print("Not enough laptops for all people")

    for person in people:
        sadnessNumber = 100 

        for laptop in available_laptops:
            if laptop.operating_system in person.preferred_operating_system:
                sadnessNumber = person.preferred_operating_system.index(laptop.operating_system)
                allocation_map[person.name] = (laptop.operating_system.value, sadnessNumber)
                available_laptops.remove(laptop)
                break
        if sadnessNumber == 100:
            allocation_map[person.name] = ("No Laptop Assigned", sadnessNumber)

    return allocation_map


personList = [
    Person(name="Aida", age=30, preferred_operating_system=[OperatingSystem.UBUNTU]),
    Person(name="Elizaveta", age=28, preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.WINDOWS, OperatingSystem.ARCH]),
    Person(name="Zahra", age=35, preferred_operating_system=[OperatingSystem.UBUNTU]),
    Person(name="Tobi", age=35, preferred_operating_system=[OperatingSystem.WINDOWS, OperatingSystem.MACOS, OperatingSystem.ARCH]),
]

laptopList = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=4, manufacturer="EDell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]

result = allocate_laptops(personList, laptopList)
lenResult = len(result)
for key, value in result.items():
    print  (f"  {key } has ** {value[0]} ** and Sadness is: {value[1]}" )



