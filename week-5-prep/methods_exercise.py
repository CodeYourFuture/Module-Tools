import datetime as dt

class Person:
    def __init__(self, name: str, dob: str, preferred_operating_system: str):
        self.name = name
        self.age = dt.date.today().year - int(dob.split("-")[0])
        
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        return self.age >= 18

imran = Person("Imran", "2004-04-18", "Ubuntu")
print(imran.is_adult())
