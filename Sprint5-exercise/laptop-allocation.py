from enum import Enum
from typing import  Dict
from dataclasses import dataclass
from scipy.optimize import linear_sum_assignment


class OperatingSystem(Enum):
    UBUNTU = "ubuntu"
    MACOS = "macos"
    ARCH = "arch linux"


@dataclass (frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: tuple[OperatingSystem,...]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def sadness(person: Person, operating_system: OperatingSystem) -> int:
  try:
        return person.preferred_operating_system.index(operating_system)
  except ValueError:
        return 100

def allocate_laptops(
    people: list[Person], laptops: list[Laptop]
) -> Dict[Person, Laptop]:
    how_many_people = len(people)
    how_many_laptops = len(laptops)
    if how_many_laptops < how_many_people:
        raise ValueError("Not enough laptops for all people")
    sadness_matrix = [[0 for i in range(how_many_laptops)] for _ in range(how_many_people)]
  
    for i, person in enumerate(people):
        for j, laptop in enumerate(laptops):
            sadness_matrix[i][j] = sadness(person, laptop.operating_system)
    # print(sadness_matrix);
    row_indexes, column_indexes = linear_sum_assignment(sadness_matrix)
    result = {}

    for row, column in zip(row_indexes, column_indexes):
        person = people[row]
        laptop = laptops[column]
        result[person] = laptop

    return result

def main() -> None:
    people = [
        Person(
            name="Imran",
            age=22,
            preferred_operating_system=(
                OperatingSystem.UBUNTU,
                OperatingSystem.ARCH,
                OperatingSystem.MACOS,
            ),
        ),
        Person(
            name="Eliza",
            age=34,
            preferred_operating_system=(OperatingSystem.UBUNTU,),
        ),
        Person(
            name="Ahmad",
            age=34,
            preferred_operating_system=(OperatingSystem.UBUNTU, OperatingSystem.MACOS,),
        ),
    ]
    laptops = [
        Laptop(
            id=1,
            manufacturer="Dell",
            model="XPS",
            screen_size_in_inches=13,
            operating_system=OperatingSystem.ARCH
        ),
        Laptop(
            id=2,
            manufacturer="HM",
            model="XPS",
            screen_size_in_inches=15,
            operating_system=OperatingSystem.MACOS,
        ),
        Laptop(
            id=3,
            manufacturer="Dell",
            model="XPS",
            screen_size_in_inches=15,
            operating_system=OperatingSystem.UBUNTU,
        ),
    ]

    print(allocate_laptops(people, laptops))


main()
