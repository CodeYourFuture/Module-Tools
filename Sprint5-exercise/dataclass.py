from datetime import date
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        current_date = date.today()
        age = current_date.year - self.date_of_birth.year

        if (current_date.month, current_date.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1

        return age >= 18


imran = Person("Imran", date(1995, 10, 16), "Ubuntu")
print(imran.is_adult())
