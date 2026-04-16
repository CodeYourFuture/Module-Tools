

from datetime import date

class Person:
    def __init__(self, name: str, dob: date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        
        age = today.year - self.dob.year
        
        # adjust if birthday hasn’t happened yet this year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age >= 18