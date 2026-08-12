class Parent:
    # Initialise the class
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

# Gets first_name and last_name from Parent class
    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    # setup Child class from the superclass Parent
    # has a new field for previous last names
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

# changes the previous lastname to a new provided lastname and adds the prev lastname to a list
    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

# creates a suffix and appends to fullname if the prev lastname List is not empty
    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

# creates an instance of Child class which inherits from Parent class
person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name()) # Elizaveta Alekseeva
print(person1.get_full_name()) # Elizaveta Alekseeva
# Changes the lastname to "Tyurina" and append Alekseeva to the previous_last_name List
person1.change_last_name("Tyurina") 
print(person1.get_name()) # Elizaveta Tyurina
print(person1.get_full_name()) # Elizaveta Tyurina (née Alekseeva)

# creates an instance of Parent class
person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name()) # Elizaveta Alekseeva
print(person2.get_full_name()) # Error: Parent class does not have the get_full_name() method/attribute and program crashes
person2.change_last_name("Tyurina") # Error: Parent class does not have the change_last_name() method, program crash
print(person2.get_name()) # Elizaveta Alekseeva
print(person2.get_full_name()) # Error: Parent class does not have the get_full_name() method/attribute, program crash
