# TASK 9
#
# Having done some research on encapsulation, think about the benefits.
#
# Think of some examples and in your own words write down some benefits and trade-offs of using encapsulation in classes:
#
# Any of, not limited to:
# Encapsulation means you can keep the functionality of a class contained
# Encapsulation means you can hide information only relevant to the class implementation
# Encapsulation lets you build a cleaner public interface
# Encapsulation makes it more difficult to misuse a class / can't use internal methods or fields
# 



# STRETCH TASK 9.1
#
# In the following  class, make the name property private
# Add a `get_name()` method to allow read-only access.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age
    
    def get_name(self):
        return self.name

    def is_adult(self):
      return self.__age >= 18

imran = Person("Imran", 22)
print(imran.get_name())
#print(imran.age) # fails
#print(imran.__age) # fails
print(imran.is_adult()) # works and prints True

eliza = Person("Eliza", 12)
print(eliza.get_name())
#print(eliza.age) # fails
#print(imran.__age) # fails
print(eliza.is_adult()) # works and prints False
