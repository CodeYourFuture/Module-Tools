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

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age >= 18

imran = Person("Imran", date(2004, 6, 28), "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
print(imran)  # Prints Person(name='Imran', age=22, preferred_operating_system='Ubuntu')

imran2 = Person("Imran", date(2004, 6, 28), "Ubuntu")
print(imran == imran2)  # Prints True
