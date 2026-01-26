#✍️exercise
#Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date 
    preferred_operating_system: str
    
    def is_adult(self) -> bool:
        today_date = date.today().year
        birth_year = self.date_of_birth.year
        age = today_date - birth_year
        return age >= 18


imran = Person("Imran", date(2000, 6, 20), "Ubuntu") 
print(imran) 
print(imran.is_adult())