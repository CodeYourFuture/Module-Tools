import datetime as dt

class Person:
    def __init__(self, name: str, dob: dt.date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system

    def get_age(self) -> int :
        today = dt.date.today()
        return today.year - self.dob.year

imran = Person("Imran", dt.date(1990,8,22), "Ubuntu")
print(imran.name)
print(imran.dob)
print(imran.get_age())



    


 


