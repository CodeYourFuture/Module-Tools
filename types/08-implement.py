import datetime

class Person:
    # The date of birth parameter can be in any format
    # but internally must use datetime in some way
    def __init__(self, name: str, dob: str, preferred_car_brand: str):
        self.name = name
        self.dob = datetime.date.fromisoformat(dob) # They should NOT pre-compute the age in the constructor
        self.preferred_car_brand = preferred_car_brand
        
    def is_adult(self):
        return datetime.date.today() - self.dob >= datetime.timedelta(days=365.25*18)
        # any age computation is valid, but it must NOT only check the year, it needs to consider days as well

def drivers_license_check(person: Person):
  if person.is_adult():
    return 'Valid drivers license'

  return 'This person is underage!'

imran = Person("Imran", "2000-01-01", "Mercedes")
eliza = Person("Eliza", "2008-10-06", "Mercedes")
print(drivers_license_check(imran)) # should return 'Valid drivers license'
print(drivers_license_check(eliza)) # should return 'This person is underage'

# TASK 8:
#
# Add an `is_adult` method into the class, and make sure your code gives the expected output.
#
# Change the `Person` class to take a date of birth using
# the standard library's `datetime.date` class
# https://docs.python.org/3/library/datetime.html#datetime.date))
# and store the `date of birth` instead of `age`.
#
# Try to run your code now and observe how this change breaks your code.
# What kind of error do you get? Is it helpful in identifying where your next change needs to be?
#
# Now update only the `is_adult` method to fix the error and check everything works correctly.
