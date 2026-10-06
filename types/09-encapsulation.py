# TASK 9
#
# Having done some research on encapsulation, think about the benefits.
#
# Think of some examples and in your own words write down some benefits and trade-offs of using encapsulation in classes:
#
#
#

# STRETCH TASK 9.1
#
# In the following  class, make the name property private
# Add a `get_name()` method to allow read-only access.

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
