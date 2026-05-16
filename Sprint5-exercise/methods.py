from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        current_date = date.today()
        age = current_date.year - self.date_of_birth.year

        if (current_date.month, current_date.day) < (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            age -= 1

        return age >= 18


imran = Person("Imran", date(1995, 10, 16), "Ubuntu")
print(imran.is_adult())
