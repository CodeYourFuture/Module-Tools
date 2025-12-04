from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.preferred_operating_system = preferred_operating_system
        #Add "date_of_birth" attribute to the "Person" class
        self.date_of_birth = date_of_birth

    def is_adult(self) ->bool:
        age_in_days = (date.today() - self.date_of_birth).days 
        age_in_years = age_in_days / 365.2425
        return age_in_years >= 18
    
    



imran = Person("Imran", date(2003,12, 3), "Ubuntu")
print(imran.is_adult())
