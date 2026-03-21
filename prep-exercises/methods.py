# ------------------------
# Q. Think of the advantages of using methods instead of free functions.
# ------------------------

# A.
# - Keeps related data together
# - Dot notation makes it clear what the operation is acting on
# - Doesn't pollute global namespace
# - Easier to maintain since all methods are inside the Class, whereas free functions can be scattered across different modules

# ------------------------
# Q. Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.

# Update the is_adult method to act the same as before.
# ------------------------

# A.

import datetime as dt


class Person:
    def __init__(self, name: str, birthdate: dt.date, preferred_operating_system: str):
        self.name = name
        self.birthdate = birthdate
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = dt.date.today()
        age = today.year - self.birthdate.year
        birthday_this_year = dt.date(
            today.year, self.birthdate.month, self.birthdate.day)
        if today < birthday_this_year:
            age -= 1
        return age >= 18


imran = Person("Imran", dt.date(2008, 3, 22), "Ubuntu")
print(imran.is_adult())
