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




# create Child object
person1 = Child("Elizaveta", "Alekseeva")
# expected state:
# first_name = Elizaveta
# last_name = Alekseeva
# previous_last_names = []

print(person1.get_name())
# exxpected: "Elizaveta Alekseeva"

print(person1.get_full_name())
# expected: "Elizaveta Alekseeva"
# (no previous last names yet)

person1.change_last_name("Tyurina")
# Expected state update:
# previous_last_names = ["Alekseeva"]
# last_name = "Tyurina"

print(person1.get_name())
# expected: "Elizaveta Tyurina"

print(person1.get_full_name())
# expected: "Elizaveta Tyurina (née Alekseeva)"



# Parent object

person2 = Parent("Elizaveta", "Alekseeva")

print(person2.get_name())
# expected: "Elizaveta Alekseeva"

print(person2.get_full_name())
# error: Parent has no method get_full_name

# program stops here 

# these lines will NOT run:
# person2.change_last_name("Tyurina")  # AttributeError
# print(person2.get_name())
# print(person2.get_full_name())