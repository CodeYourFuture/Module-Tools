import datetime


class Person:
    def __init__(
        self, name: str, date_of_birth: datetime.date, preferred_operating_system: str
    ):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        print(age)
        return age >= 18


imran = Person("Imran", datetime.date(1998, 4, 3), "Ubuntu")
print(imran.is_adult())
eliza = Person("Eliza", datetime.date(2013, 3, 17), "Arch Linux")
print(eliza.is_adult())
