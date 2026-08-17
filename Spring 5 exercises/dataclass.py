from dataclasses import dataclass
from datetime import date

@dataclass
class Person:
    name : str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool :
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age-=1

        return age>=18   

amy= Person("Amy", date(2011,11,23), "Ubuntu")  
amy2= Person("Amy", date(2011,11,23), "Ubuntu") 

print(amy)
print(amy2)
print(amy==amy2)
print(amy.is_adult())


           
