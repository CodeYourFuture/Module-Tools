# ✍️exercise
# Play computer with this code. Predict what you expect each line will do. Then run the code and check your predictions.
#  (If any lines cause errors, you may need to comment them out to check later lines).

class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

# Child class (inherits from Parent)
class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)    # Call Parent constructor
        self.previous_last_names: list[str] = []  # New property (only Child has this)


    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name) # Save old last name
        self.last_name = last_name  # Update to new last name

    def get_full_name(self) -> str:   # Extra method only in Child
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"
    

person1 = Child("Elizaveta", "Alekseeva")
print(person1.get_name()) # Inherited method from Parent 
# Output: Elizaveta Alekseeva

print(person1.get_full_name()) 
#  Method from Child , 
# Output: Elizaveta Alekseeva


person1.change_last_name("Tyurina") 
# Change last name

print(person1.get_name()) 
# Parent method still works , 
# Output: Elizaveta Tyurina (née Alekseeva)

print(person1.get_full_name())


# Using Parent
person2 = Parent("Elizaveta", "Alekseeva")

# Works (Parent method), 
# Output: Elizaveta Alekseeva
print(person2.get_name())


# print(person2.get_full_name()) 
# ERROR: Parent has no method "get_full_name"

# person2.change_last_name("Tyurina") 
# ERROR: Parent has no method "change_last_name"

print(person2.get_name())
# print(person2.get_full_name())






# Inheritance allows a class (Child) to reuse and extend another class (Parent).
# When calling a method, Python first checks the subclass, then the superclass.
# The Child can add or override methods, but the Parent cannot access Child-specific methods.

# Difference between inheritance and composition:
# - Inheritance: "is-a" (Child IS a Parent)
# - Composition: "has-a" (Object HAS another object)
