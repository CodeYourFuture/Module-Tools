#Change the Person class to take a date of birth (using the standard library’s datetime.date class) and
#store it in a field instead of age.

#Update the is_adult method to act the same as before.

from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.preferred_operating_system = preferred_operating_system
        #Add "date_of_birth" attribute to the "Person" class
        self.date_of_birth = date_of_birth

    def is_adult(self):
        age_in_days = (date.today() - self.date_of_birth).days 
        age_in_years = age_in_days / 365.2425
        return age_in_years >= 18
    
    





imran = Person("Imran", 22, "Ubuntu")
print(imran.is_adult())


