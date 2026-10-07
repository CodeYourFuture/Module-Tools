class Parent:

    # this is constructor and sets attributes
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    # this is a method that gets name and last name
    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Child inherits attributes and methods from Parent
class Child(Parent):
    # child class constructor
    def __init__(self, first_name: str, last_name: str):

        # Call the Parent constructor to initialise first_name and last_name
        super().__init__(first_name, last_name)
        self.previous_last_names: list[str] = []

    # Save the current last name, then change it to the new last name
    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    # this method gets the fullname
    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


# creating object of Child class
person1 = Child("Elizaveta", "Alekseeva")
# prints the name of person1 which will be (Elizaveta Alekseeva)
print(person1.get_name())
# # Prints the new full name and the previous last name
print(person1.get_full_name())
# prints the new last name by calling the change_last_name method with a new parameter
person1.change_last_name("Tyurina")
# here again it prints the name of person1
print(person1.get_name())
# prints the fullname of person1, but this time the last name ll be other than before
print(person1.get_full_name())

# same cycle with the object of parent class this time
person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
#print(person2.get_full_name())
#person2.change_last_name("Tyurina")
print(person2.get_name())
#print(person2.get_full_name())
