# The advantage of using methods instead of free functions.
# 1. Encapsulation & Organization: methods group behavior directly with the data it operates on the object.
# 2. State management: methods have direct access to 'self'.
# 3. Readibility.

from datetime import date

class Person:
    def __init__(self, name: str, birth_date: date, preferred_operating_system: str):
        self.name = name
        self.birth_date = birth_date
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.birth_date.year
        birthday_has_passed: bool = (today.month, today.day) >= (self.birth_date.month, self.birth_date.day)
        
        if not birthday_has_passed:
            age -= 1
        return age >= 18

imran = Person("Imran", date(2000, 5, 20), "Ubuntu")
print(f"Is Imran an adult? {imran.is_adult()}")