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
print(person1.get_name())
print(person1.get_full_name())
person1.change_last_name("Tyurina")
print(person1.get_name())
print(person1.get_full_name())

person2 = Parent("Elizaveta", "Alekseeva")
print(person2.get_name())
if isinstance(person2, Child):
    print(person2.get_full_name())
    person2.change_last_name("Tyurina")
    print(person2.get_name())
    print(person2.get_full_name())
else:
    print("Parent does not have get_full_name() or change_last_name().")

# Predictions vs actual output (play computer):
# 1) Child inherits get_name() from Parent.
# 2) Child-specific get_full_name() shows the maiden name after changing last name.
# 3) Parent supports get_name() only; Child-only methods are unavailable on Parent.

""" When I played computer, I predicted that Child would inherit get_name() from Parent, so person1.get_name() should work exactly like in Parent, while person1.get_full_name() would only exist on Child and add extra detail after a last-name change. Running the code confirmed this: before changing the name, both methods show “Elizaveta Alekseeva”, and after change_last_name("Tyurina"), get_full_name() includes the maiden-name suffix (née Alekseeva). For person2 (a Parent), only get_name() is available, which shows that inheritance gives Child all parent behavior plus additional child-specific methods, but not the other way around. """
