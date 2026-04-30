from dataclasses import dataclass
from typing import List
from datetime import date


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    children: List["Person"]

    def getAge(self) -> int:
        current_date = date.today()
        full_years = current_date.year - self.date_of_birth.year
        if (current_date.month < self.date_of_birth.month) or (
            current_date.month == self.date_of_birth.month
            and current_date.day < self.date_of_birth.day
        ):
            full_years -= 1
        return full_years


fatma = Person(name="Fatma", date_of_birth=date(2020, 4, 12), children=[])
aisha = Person(name="Aisha", date_of_birth=date(2024, 7, 5), children=[])

imran = Person(name="Imran", date_of_birth=date(2000, 1, 30), children=[fatma, aisha])


def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.getAge()})")


print_family_tree(imran)
