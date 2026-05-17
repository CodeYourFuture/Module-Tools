from datetime import date
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year
        
        # Check if birthday has occurred this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        
        return age >= 18

imran = Person("Imran", date(2002, 5, 15), "Ubuntu")
print(imran.name)
print(imran.is_adult())

eliza = Person("Eliza", date(1990, 3, 20), "Arch Linux")
print(eliza.name)
print(eliza.is_adult())