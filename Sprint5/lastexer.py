class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:  # get name is a method of class parent 
        return f"{self.first_name} {self.last_name}"


class Child(Parent):   #childclass of parent
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)  #superclass constructor intialised in childclass
        self.previous_last_names = []   #intialised a new attribute

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name) #append previous lastname to the previous_last_names[]
        self.last_name = last_name #set the new one as last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:  #if last_name has been changes, it adds the previous last name as a suffix to the new one 
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
print(person2.get_full_name())  #childclass method
person2.change_last_name("Tyurina") #childclass method
print(person2.get_name())
print(person2.get_full_name())