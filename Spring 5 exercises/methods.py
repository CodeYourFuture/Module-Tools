 # Think of the advantages of using methods instead of free functions:
 # Better organization, More readable code, Easier maintenance,Better editor support (autocomplete),Code reuse across all instances of the class
 # Ease of documentation: Related data and behavior are grouped together, making the class easier to understand.
 # Encapsulation: The implementation can change without affecting the rest of the program, as long as the method's interface stays the same.

from datetime import date


class Person:
    def __init__(self, name: str, date_of_birth:date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        today= date.today()

        age=today.year- self.date_of_birth .year

        if(today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
           age-=1 

        return age>=18
    
amy = Person("Amy",date(2003,1,5), "Ubuntu")
eliza = Person("Eliza",date(2012,11,25), "Ubuntu")

print(amy.is_adult())
print(eliza.is_adult())