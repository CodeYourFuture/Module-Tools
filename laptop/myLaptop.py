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

    allocateLp = {}
    lpNewList = laptops.copy()

    if len(laptops) < len(people):
        print("Not enough laptops for all people")

    for person in people:
        sadnessNumber = 100 

        for lp in lpNewList:
            if lp.operating_system in person.preferred_operating_system:
                sadnessNumber = person.preferred_operating_system.index(lp.operating_system)
                allocateLp[person.name] = (lp.operating_system.value, sadnessNumber)
                lpNewList.remove(lp)
                break
        if sadnessNumber == 100:
            allocateLp[person.name] = ("No Laptop Assigned", sadnessNumber)

    return allocateLp


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



