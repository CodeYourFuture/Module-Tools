from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
from itertools import permutations


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def sadness(person: Person, laptop: Laptop) ->int:
    try:
        return person.preferred_operating_system.index(laptop.operating_system)
    except ValueError:
        return 100


def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:

    best_scenario_assignment = None
    best_total_sadness = float("inf")

    for scenario in scenarios(laptops):
        total_sadness = 0

        #find the sadness level for each scenario
        for person, laptop in zip(people, scenario):
            total_sadness += sadness(person, laptop)

        #Check if this is the best scenario so far
        if total_sadness < best_total_sadness:
            best_total_sadness = total_sadness
            best_scenario_assignment = scenario


