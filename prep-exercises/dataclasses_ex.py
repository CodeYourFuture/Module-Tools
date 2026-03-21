# ------------------------
# Q. Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

# Re-add the is_adult method to it.
# ------------------------

# A.

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
        birthday_this_year = dt.date(
            today.year, self.birthdate.month, self.birthdate.day)
        if today < birthday_this_year:
            age -= 1
        return age >= 18


imran = Person("Imran", dt.date(2008, 3, 21), "Ubuntu")
print(imran.is_adult())
