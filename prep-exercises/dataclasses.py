# --- Exercise ---
# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.

# Re-add the is_adult method to it.

# --- Solution ---
import datetime

class Person:
    def __init__(self, name: str, date_of_birth: datetime.date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(person: Person) -> bool:
        today = datetime.date.today()
        age = today.year - person.date_of_birth.year
        if today.month < person.date_of_birth.month or (today.month == person.date_of_birth.month and today.day < person.date_of_birth.day):
            age -= 1
        return age >= 18   

