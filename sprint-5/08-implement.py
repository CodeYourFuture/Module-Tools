class Person:
    def __init__(self, name: str, age: int, preferred_car_brand: str):
        self.name = name
        self.age = age
        self.preferred_car_brand = preferred_car_brand

def drivers_license_check(person: Person):
  if person.is_adult() == True:
    return 'Valid drivers license'

  return 'This person is underage!'

imran = Person("Imran", 22, "Mercedes")
print(drivers_license_check(imran)) # should return 'Valid drivers license'

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
