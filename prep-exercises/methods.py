# Think of the advantages of using methods instead of free functions. Write them down in your notebook.
# It is object oriented. The same method can be shared between the same class.
# It is more obvious to understand the purpose of the methods than a free function 

import datetime as dt

class Person:
    def __init__(self, name: str, date_of_birth: str, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = dt.date.fromisoformat(date_of_birth)
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = dt.datetime.today()

        age_in_year = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age_in_year -= 1
        return age_in_year >= 18

imran = Person("Imran", "2000-10-20", "Ubuntu")
print(imran.is_adult())
