from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        current_date = date.today()
        full_years = current_date.year - self.date_of_birth.year
        if (current_date.month < self.date_of_birth.month) or (
            current_date.month == self.date_of_birth.month
            and current_date.day < self.date_of_birth.day
        ):
            full_years -= 1
        return full_years >= 18


imran = Person("Imran", date(2008, 1, 30), "Ubuntu")
print(imran)
print("Imran is adult: " + str(imran.is_adult()))
