from dataclasses import dataclass
from typing import List
from enum import Enum


class OperatingSystem(Enum):
    UBUNTU = "Ubuntu"
    MAC = "Mac"
    WINDOWS = "Windows"


@dataclass
class Person:
    name: str
    age: int
    preferred_os: OperatingSystem


@dataclass
class Laptop:
    model: str
    os: OperatingSystem


def get_matching_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    matches = []

    for laptop in laptops:
        if laptop.os == person.preferred_os:
            matches.append(laptop)

    return matches


laptops = [
    Laptop("Dell", OperatingSystem.UBUNTU),
    Laptop("MacBook", OperatingSystem.MAC),
    Laptop("HP", OperatingSystem.WINDOWS),
]

person = Person("Ali", 22, OperatingSystem.UBUNTU)

print(get_matching_laptops(laptops, person))