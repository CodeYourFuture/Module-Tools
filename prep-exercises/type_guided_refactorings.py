from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: List[str]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        for system in person.preferred_operating_systems:
            if laptop.operating_system == system:
                possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_systems=["Ubuntu", "Arch Linux", "macOS", "Windows"]),
    Person(name="Eliza", age=34, preferred_operating_systems=["Arch Linux", "Ubuntu", "macOS", "Windows"]),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
]

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")

    system_list = person.preferred_operating_systems
    preference_sentences: List[str] = ["prefers {} most of all", ", and then {}", ", but will not use {}"]
    statement: str = f'{person.name} '

    if len(system_list) != 0:
        for index, system in enumerate(system_list):
            if index == 0:
                statement += preference_sentences[index].format(system)
            elif index == len(system_list) - 1:
                statement += preference_sentences[-1].format(system)
            else:
                statement += preference_sentences[1].format(system)
    print(statement)
