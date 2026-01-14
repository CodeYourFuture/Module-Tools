from datetime import date

class Person:
    def __init__(self, name: str, dOB: date, preferred_operating_system: str):
        self.name = name
        self.dOB = dOB
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)
        return self.dOB <= eighteen_years_ago

imran = Person("Imran", date(1992, 7, 21), "Ubuntu")
print(imran.name)

print(imran.is_adult())

