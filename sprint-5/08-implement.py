class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.is_adult())

# Task:
# 1. Add the `drivers_license_check` free function and the `is_adult` method into the code
# 	Make sure your code currently gives the expected output.
#
# 2. Change the `Person` class to take a date of birth
#	Use the standard library's `datetime.date` class
#	https://docs.python.org/3/library/datetime.html#datetime.date
#	Store the `date of birth` in a field instead of `age` (it should be a `str`)
#
# 3. Try to run your code
#	How does this change break your code.
#	What kind of error do you get?
#	Is it helpful in identifying where your next change needs to be?
#	Type your thoughts here:
#
#
#
#
# 4. Update the `is_adult` method so the error is fixed.
#	Using the `drivers_license_check` function check everything runs as expected

