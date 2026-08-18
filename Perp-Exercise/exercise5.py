import datetime as dt
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    dob: dt.date
    preferred_os:str
      
    def get_age(self) -> int :
        today = dt.date.today()
        return today.year - self.dob.year

imran = Person("Imran", dt.date(1990,8,22), "Ubuntu")
print(imran.name)
print(imran.dob)
print(imran.get_age())



    


 


