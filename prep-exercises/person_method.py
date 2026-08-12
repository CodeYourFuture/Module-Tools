import datetime as dt

class Person:
    def __init__(self, name: str, dob: dt.date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = dt.date.today()

        age = today.year - self.dob.year

        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age >= 18

imran = Person("Imran", dt.date(1998, 11, 13), "Ubuntu")
print(imran.is_adult())
