#Change the Person class to take a date of birth (using the standard library’s datetime.date class) and
#store it in a field instead of age.

#Update the is_adult method to act the same as before.

from datetime import date


class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        return self.age >= 18
    
# Add date_of_birth attribute to the Person class
setattr(Person, "date_of_birth", "date_of_birth")


imran = Person("Imran", 22, "Ubuntu")
print(imran.is_adult())


