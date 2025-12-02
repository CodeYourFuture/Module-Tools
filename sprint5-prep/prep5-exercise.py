from dataclasses import dataclass
import datetime
@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: datetime.date
    preferred_operating_system: str
    def is_adult(self) -> bool :
      today=datetime.date.today()
      age=today.year-self.date_of_birth.year
      if(today.month,today.day)<(self.date_of_birth.month,self.date_of_birth.day) :
         age -=1
      return age>=18
imran = Person("Imran", datetime.date(2007,12,16), "Ubuntu")  
print(imran) 
print(imran.is_adult())

