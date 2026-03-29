# ✍️exercise
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.
# Re-add the is_adult method to it.

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str


    def is_adult(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) <  (self.date_of_birth.month, self.date_of_birth.day):
            age = age - 1

        return age >= 18

imran = Person("Imran", date(2000,5,12), "Ubuntu")
print(imran)  

imran2 = Person("Imran",date(2000,5,12), "Ubuntu")
print(imran == imran2)  # Prints True
