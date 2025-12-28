# play computer game with the code below and predict what you expect each line will do. Then run the code and check your prediction (If any lines cause errors, you may need to comment them out to check later lines).

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names: list[str] = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name()) #works because get_name is inherited from Parent.
print(person1.get_full_name()) # get_full_name() works, exist in child.
person1.change_last_name("Tyurina") #change_last_name("Tyurina") works, exist in child..
print(person1.get_name()) # works because it comes from Parent.get_name.
print(person1.get_full_name())# works because it comes from Parent.get_name.


person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name()) # works because it is the Parent class.
print(person1.get_full_name())
# print(person2.get_full_name()) #get_full_name is defined only in child
# person2.change_last_name("Tyurina") #change_last_name is defined only in child not in parent
print(person2.get_name())
# print(person2.get_full_name()) #get_full_name is defined only in child not in parent


# ===============What I learned from playing computer game with above code.

# 1. Objects can only call methods they actually have inside them.
# - Creating a parent object does not automatically give the child its behavior

# =====================================================================
#2. Inheritance is "is-a", not "might-be" i.e
# A child is a parent(here the child can inherit freely from the father.)
# A parent is NOT a child(i.e a parent does not inherit from the child)
