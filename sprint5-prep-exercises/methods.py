"""Examples of classes and methods.

A function is a reusable block of code that is defined on its own.
A method is a function that belongs to a class and is called on an object.

In this file, `Person.is_adult()` is a method because it belongs to the
`Person` class, while `date.today()` is a method on the `date` class.
"""

from datetime import date


class Person:
	def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str) -> None:
		self.name = name
		self.date_of_birth = date_of_birth
		self.preferred_operating_system = preferred_operating_system

	def is_adult(self) -> bool:
		today = date.today()
		has_had_birthday_this_year = (today.month, today.day) >= (
			self.date_of_birth.month,
			self.date_of_birth.day,
		)
		age = today.year - self.date_of_birth.year
		if not has_had_birthday_this_year:
			age -= 1
		return age >= 18


imran = Person("Imran", date(2002, 6, 15), "Ubuntu")
eliza = Person("Eliza", date(1990, 11, 20), "Arch Linux")

print(imran.name)
print(imran.is_adult())
print(eliza.name)
print(eliza.is_adult())
