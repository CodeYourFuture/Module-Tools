from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_car_brand: str

    def is_adult(self):
        return self.age >= 18
      
    def greet(self):
        return f"Hello {self.name}!"

def drivers_license_check(person: Person):
  if person.is_adult():
    return 'Valid drivers license'

  return 'This person is underage!'

imran = Person(name="Imran", age=22, preferred_car_brand="Mercedes")
print(imran) # should print out all fields
print(imran.greet())
print(drivers_license_check(imran)) # should return 'Valid drivers license'


# TASK 10.1:
# Convert the above `Person` class into a value type using `@dataclass`
# so you can print the class (and see it's type and properties)
# and compare class instances that are identical.
# Make sure your `is_adult` method and `drivers_license_check` free function both work.

# TASK 10.2:
# Make a new method on your Person class - `greet()` which should return `"Hello <person name>!"` when used.

# TASK 10.3:
# Read the @dataclass documentation here: https://docs.python.org/3/library/dataclasses.html
# Explain what `frozen=True` does to the class?
# What other options could you play around with and explore? Offer suggestions for any that would be useful here.

# Any of the following, not limited to:
# Frozen=True means a class instance is read only / you can't change fields/attributes/properties
# Frozen=True means you need to define fields in the class first
# Frozen=True means you can't add or remove additional fields/attributes/properties

# This is incorrect:
# frozen=True adds a constructor (all @dataclass does this, not frozen)
# frozen=True allows you to print a class (all @dataclass does this, not frozen)

# Any of the following, not limited to:
# eq for allowing to compare people
# order forallowing us to order people in a custom order, e.g. by age, name, preferred car
# or any other valid context and explanation