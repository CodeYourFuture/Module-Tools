# ✍️exercise
# Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.
# Update the is_adult method to act the same as before.
from datetime import date
class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        
        age = today.year - self.date_of_birth.year
        
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age >= 18



imran = Person("Imran", date(2002, 5, 10), "Ubuntu")
eliza = Person("Eliza", date(1990, 8, 3), "Arch Linux")

print(imran.is_adult())
print(eliza.is_adult())









# ✍️exercise
# Think of the advantages of using methods instead of free functions.
#  Write them down in your notebook.
# Encapsulation 
# The class controls its own logic
# Example: You change from age → date_of_birth
# Only the class needs to change,  External code still works:person.is_adult()
# Methods = behavior belongs to the object