class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def is_adult(self):
      return self.__age >= 18

imran = Person("Imran", 22)
print(imran.name)
print(imran.age) # fails
print(imran.__age) # fails
print(imran.is_adult()) # works and prints True

eliza = Person("Eliza", 12)
print(eliza.name)
print(eliza.age) # fails
print(imran.__age) # fails
print(eliza.is_adult()) # works and prints False

# Task 9
# Read through Python encapsulation
# https://www.w3schools.com/python/python_encapsulation.asp
# and think about some of the benefits that encapsulation can add to a class.
#
# Do some further research of your own to learn about encapsulation.
#
# Think of some examples and in your own words write down some benefits and trade-offs of using encapsulation in classes:
#
#
#

# Stretch Task
# Make the name property private, and add a get_name() method to make it read only.
