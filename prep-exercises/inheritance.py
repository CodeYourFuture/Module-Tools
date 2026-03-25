# ------------------------
# Play computer with this code. Predict what you expect each line will do. Then run the code and check your predictions. (If any lines cause errors, you may need to comment them out to check later lines).
# ------------------------

# A.

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

    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


person1 = Child("Elizaveta", "Alekseeva")
# Predict: person1 has first_name="Elizaveta", last_name="Alekseeva", previous_last_names=[]

print(person1.get_name())
# Checked: prints "Elizaveta Alekseeva"

print(person1.get_full_name())
# Predict + checked: prints "Elizaveta Alekseeva"

person1.change_last_name("Tyurina")
# Predict: previous_last_names becomes ["Alekseeva"], last_name becomes "Tyurina"

print(person1.get_name())
# Predict + checked: prints "Elizaveta Tyurina"

print(person1.get_full_name())
# Predict + checked: prints "Elizaveta Tyurina (née Alekseeva)"

person2 = Parent("Elizaveta", "Alekseeva")
# Predict: person2 has first_name and last_name only

print(person2.get_name())
# Predict + checked: prints "Elizaveta Alekseeva"

# print(person2.get_full_name())
# Predict + checked: AttributeError, because Parent has no get_full_name method

# person2.change_last_name("Tyurina")
# Predict + checked: AttributeError, because Parent has no change_last_name method

print(person2.get_name())
# Predict + checked: still prints "Elizaveta Alekseeva"

# print(person2.get_full_name())
# Predict + checked: AttributeError again for missing Parent.get_full_name
