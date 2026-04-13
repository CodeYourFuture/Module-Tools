from typing import List

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: List[str] = []

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name())
print(person1.get_full_name())
person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
# print(person2.get_full_name())
# person2.change_last_name("Tyurina")
print(person2.get_name())
# print(person2.get_full_name())


# Predictions:
# person 1 should be able to print both name and full name as Elizaveta Alekseeva
# and should be able to print both name Elizaveta Tyurina and full name Elizaveta Tyurina (née Alekseeva) after changing last name to Tyurina
# because it was created in class Child which inherits get_name from class Parent
# 
# In contracts, person 2 is able to print name as Elizaveta Alekseeva
# but shouldn't be able to print full name as it was create in class Parent, which does not have method get_full_name
# and couldn't be able to change last name to Tyurina, so the name stays the same Elizaveta Alekseeva
# and it still won't be able to print full name even after the attempt of change last name 
