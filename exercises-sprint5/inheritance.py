""" ✍️exercise
Play computer with this code. Predict what you expect each line will do. Then run the code and check your predictions. (If any lines cause errors, you may need to comment them out to check later lines).
"""

# PREDICTION: This defines a base class called Parent
class Parent:
     # PREDICTION: Constructor that sets first_name and last_name attributes
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

# PREDICTION: Method that returns full name as "first last"
    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

# PREDICTION: Child class inherits everything from Parent class
class Child(Parent):
 # PREDICTION: Constructor calls parent's constructor then adds new attribute    
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name) # PREDICTION: Calls Parent.__init__
        self.previous_last_names = []  # PREDICTION: Creates empty list for this instance

# PREDICTION: Method to change last name and track previous names
    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

# PREDICTION: Method that returns full name with maiden name note if changed
    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"
    

# PREDICTION: Creates Child instance with names "Elizaveta" "Alekseeva"
person1 = Child("Elizaveta", "Alekseeva")
# PREDICTION: Prints "Elizaveta Alekseeva" (calls inherited get_name() from Parent)
print(person1.get_name())
# PREDICTION: Prints "Elizaveta Alekseeva" (no suffix since no name change yet)
print(person1.get_full_name())
# PREDICTION: Changes last name to "Tyurina", adds "Alekseeva" to previous_last_names
person1.change_last_name("Tyurina")
# PREDICTION: Prints "Elizaveta Tyurina" (updated last name)
print(person1.get_name())
# PREDICTION: Prints "Elizaveta Tyurina (née Alekseeva)" (shows maiden name)
print(person1.get_full_name())


# PREDICTION: Creates Parent instance (NOT Child) with same names
person2 = Parent("Elizaveta", "Alekseeva")
# PREDICTION: Prints "Elizaveta Alekseeva" (Parent has get_name() method)
print(person2.get_name())
# PREDICTION:  ERROR! Parent class doesn't have get_full_name() method
print(person2.get_full_name())
# PREDICTION:  ERROR! Parent class doesn't have change_last_name() method
person2.change_last_name("Tyurina")
# PREDICTION: Won't reach this line due to previous error
print(person2.get_name())
# PREDICTION: Won't reach this line due to previous error
print(person2.get_full_name())