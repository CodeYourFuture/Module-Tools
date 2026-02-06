#Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an
#int for age.

#Re-add the is_adult method to it.


from datetime import date
from dataclasses import dataclass

@dataclass
class Person:
        name: str
        date_of_birth: date
        preferred_operating_system: str
        
        def is_adult(self) ->bool:
            age_in_days = (date.today() - self.date_of_birth).days 
            age_in_years = age_in_days / 365.2425
            return age_in_years >= 18
    
    

imran = Person("Imran", date(2003,12, 3), "Ubuntu")
print(imran.is_adult())
