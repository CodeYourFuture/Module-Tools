from dataclasses import dataclass
from datetime import date

@dataclass (frozen=True)
class Person:
    name: str
    DOB: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)
        return self.DOB <= eighteen_years_ago

imran = Person("Imran", date(1992, 7, 21), "Ubuntu")
print(imran.name)

imran2 = Person("Imran", date(1992, 7, 21), "Ubuntu")
print(imran == imran2) 

eliza = Person("Eliza", date(1982, 4, 5), "Arch Linux")
print(eliza.name)


print(imran.is_adult())
print(eliza.is_adult())
