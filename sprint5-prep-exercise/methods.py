

from datetime import date

class Person:
    # __init__ is a method (a function inside a class)
    def __init__(self, name: str, dob: date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system

    # is_adult is also a method
    def is_adult(self) -> bool:
        today = date.today()
        
        age = today.year - self.dob.year
        
        # adjust if birthday hasn’t happened yet this year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age >= 18
    

# Function:
# A reusable block of code that exists independently.
# This is a normal function:
# def greet():
#     print("Hello")

# Method:
# A function that belongs to a class and usually works with object data using `self`.

