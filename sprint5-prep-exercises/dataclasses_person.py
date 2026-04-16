from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    dob: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        
        age = today.year - self.dob.year
        
        # adjust if birthday hasn’t happened yet this year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age >= 18
    

imran = Person("Imran", date(2003, 5, 10), "Ubuntu")

print(imran)
print(imran.is_adult())