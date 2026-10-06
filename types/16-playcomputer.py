class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"
    
# TASK 16:
# Play computer with this code
# Describe what is happening and why on each line below here
# If any lines cause errors, comment out the line and explain why the error happens

person1 = Child("Elizaveta", "Alekseeva") # instantiate a new Child, which is a subclass of Parent
print(person1.get_name()) # Look for get_name on Child, it's not present, so call it on Parent
print(person1.get_full_name()) # Look for get_full_name on Child and call it
person1.change_last_name("Tyurina") # Look for change_last_name on child, call it, and update both the name fields in Parent and the list of previous_last_names within Child
print(person1.get_name()) # Look for get_name on Child, it's not present, so call it on Parent, and use the updated values 
print(person1.get_full_name()) # Look for get_full_name on Child and call it, it will print the original name as well

person2 = Parent("Elizaveta", "Alekseeva") # instantiate a new parent
print(person2.get_name()) # look for get_name on parent, call it
# print(person2.get_full_name())  # look for get_full_name on parent, it doesn't exist, so error
# person2.change_last_name("Tyurina") # look for change_last_name on parent, it doesn't exist, so error
print(person2.get_name()) # look for get_name on parent, call it, value will remain unchanged
# print(person2.get_full_name()) # look for get_full_name on parent, it doesn't exist, so error
