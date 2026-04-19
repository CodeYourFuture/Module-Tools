from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    children: List["Person"]

    @property
    def age(self) -> int:
        today = date.today()
        has_had_birthday_this_year = (today.month, today.day) >= (
            self.date_of_birth.month,
            self.date_of_birth.day,
        )
        years = today.year - self.date_of_birth.year
        if not has_had_birthday_this_year:
            years -= 1
        return years


fatma = Person(name="Fatma", date_of_birth=date(2017, 5, 3), children=[])
aisha = Person(name="Aisha", date_of_birth=date(2019, 9, 12), children=[])

imran = Person(name="Imran", date_of_birth=date(1991, 2, 10), children=[fatma, aisha])

def print_family_tree(person: Person) -> None:
    print(person.name)
    for child in person.children:
        print(f"- {child.name} ({child.age})")

print_family_tree(imran)