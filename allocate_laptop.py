from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Tuple, Optional

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

def norm_os_values(value: str) -> OperatingSystem:
    value = value.strip().lower()
    if value == "ubuntu":
        return OperatingSystem.UBUNTU
    if value == "arch linux":
        return OperatingSystem.ARCH
    if value == "macos":
        return OperatingSystem.MACOS
    raise ValueError(f"Unknown OS: {value}")


people = [
    Person(name="Imran", age=22, preferred_operating_systems=[norm_os_values("Ubuntu"), norm_os_values("Arch Linux")]),
    Person(name="Eliza", age=34, preferred_operating_systems=[norm_os_values("Arch Linux"), norm_os_values("macOS"), norm_os_values("Ubuntu")]),
    Person(name="Ira", age=21, preferred_operating_systems=[norm_os_values("Ubuntu"), norm_os_values("Arch Linux")]),
    Person(name="Anna", age=34, preferred_operating_systems=[norm_os_values("Ubuntu"), norm_os_values("macOS")]),
    Person(name="Nahimn", age=42, preferred_operating_systems=[norm_os_values("Ubuntu"), norm_os_values("Arch Linux")])
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=norm_os_values("Arch Linux")),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=norm_os_values("Ubuntu")),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=norm_os_values("ubuntu")),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=norm_os_values("macOS")),
]


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Tuple[str, int], int]:
    sadness_table: Dict[Tuple[str, int], int] = {}
    for person in people:
        for laptop in laptops:
            if laptop.operating_system in person.preferred_operating_systems:
                index = person.preferred_operating_systems.index(laptop.operating_system)
                sadness = index
            else:
                sadness = 100
            sadness_table[(person.name, laptop.id)] = sadness
    return sadness_table


sadness_table = allocate_laptops(people, laptops)

allocation_list: List[Tuple[str, Optional[int], int]] = []
allocated_laptops: set[int] = set()
allocated_persons: set[str] = set()
total_happiness: int = 0

for (person_name, laptop_id), sadness in sorted(sadness_table.items(), key=lambda value: value[1]):
    if laptop_id in allocated_laptops:
        continue
    if person_name in allocated_persons:
        continue
    allocation_list.append((person_name, laptop_id, sadness))
    allocated_laptops.add(laptop_id)
    allocated_persons.add(person_name)
    total_happiness += sadness
    print(f"{person_name} got laptop {laptop_id}")

    
for person in people:
    if person.name not in allocated_persons:
        print(f"{person.name} did not get laptop")
print(f"Total happiness: {total_happiness}")

print(allocation_list)

