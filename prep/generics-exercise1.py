from dataclasses import dataclass
from typing import List
from datetime import date


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    children: List["Person"]

    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1
        return age


fatma = Person(name="Fatma", date_of_birth=date(2015, 7, 22), children=[])
aisha = Person(name="Aisha", date_of_birth=date(2018, 3, 10), children=[])

imran = Person(name="Imran", date_of_birth=date(1985, 5, 15), children=[fatma, aisha])


def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")


print_family_tree(imran)
