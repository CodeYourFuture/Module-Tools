import datetime as dt
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    birthdate: dt.date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = dt.date.today()
        age = today.year - self.birthdate.year

        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1

        return age >= 18


imran = Person("Imran", dt.date(2000, 8, 6), "Ubuntu")

print(imran.is_adult())