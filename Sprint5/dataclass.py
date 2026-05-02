from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    birth_date: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.birth_date.year
        
        birthday_has_passed = (today.month, today.day) >= (self.birth_date.month, self.birth_date.day)
        
        if not birthday_has_passed:
            age -= 1
            
        return age >= 18

imran1 = Person("Imran", date(2000, 5, 20), "Ubuntu")
imran2 = Person("Imran", date(2000, 5, 20), "Ubuntu")

print(imran1)  
print(f"Are they equal? {imran1 == imran2}") 
print(f"Is Imran an adult? {imran1.is_adult()}")