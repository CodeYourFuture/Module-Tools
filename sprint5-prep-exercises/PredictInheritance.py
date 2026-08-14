# Parent class stores a person's first name and last name
class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    # Returns the person's first and last name together
    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

# Child inherits the fields and methods from Parent
# It also allows the person to change their last name
class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []
    # Changes the last name and saves the old name
    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name
   # Returns the current name and the original last name
    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"
# Create child object
person1 = Child("Elizaveta", "Alekseeva")
# Child inherits get_name() from Parent
# Output: Elizaveta Alekseeva
print(person1.get_name())
# Child has its own get_full_name() method
# Output: Elizaveta Alekseeva
print(person1.get_full_name())
# Change the last name 
person1.change_last_name("Tyurina")
# The current last name is now Tyurina
# Output: Elizaveta Tyurina
print(person1.get_name())
# Shows the new name and the previous last name
# Output: Elizaveta Tyurina (née Alekseeva)
print(person1.get_full_name())
# Create a Parent object
person2 = Parent("Elizaveta", "Alekseeva")
# Parent has get_name(), so this works
# Output: Elizaveta Alekseeva
print(person2.get_name())
# This causes an AttributeError because Parent
# does not have a get_full_name() method
print(person2.get_full_name())
# This also causes an AttributeError because Parent
# does not have a change_last_name() method
person2.change_last_name("Tyurina")
# get_name() still works because it belongs to Parent
# Output: Elizaveta Alekseeva
print(person2.get_name())
# This would cause another AttributeError
# because get_full_name() only exists in Child
print(person2.get_full_name())