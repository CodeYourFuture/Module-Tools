from enum import Enum
from dataclasses import dataclass


class OS(Enum):
    UBUNTU = "Ubuntu"
    MAC = "Mac"
    WINDOWS = "Windows"


@dataclass
class Laptop:
    model: str
    os: OS


@dataclass
class Person:
    name: str
    age: int
    preferred_os: OS


laptops = [
    Laptop("Dell", OS.UBUNTU),
    Laptop("MacBook", OS.MAC),
    Laptop("HP", OS.WINDOWS),
]

person = Person("Ali", 22, OS.UBUNTU)


def match(laptops, person):
    result = []
    for l in laptops:
        if l.os == person.preferred_os:
            result.append(l)
    return result


print(match(laptops, person))