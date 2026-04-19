from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        has_had_birthday_this_year = (today.month, today.day) >= (
            self.date_of_birth.month,
            self.date_of_birth.day,
        )
        age = today.year - self.date_of_birth.year
        if not has_had_birthday_this_year:
            age -= 1
        return age >= 18


imran = Person("Imran", date(2002, 6, 15), "Ubuntu")
imran2 = Person("Imran", date(2002, 6, 15), "Ubuntu")
eliza = Person("Eliza", date(1990, 11, 20), "Arch Linux")

print(imran)
print(imran == imran2)
print(imran.is_adult())
print(eliza.is_adult())