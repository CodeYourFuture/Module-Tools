# Add the is_adult code to the file you saved earlier.

# Run it through mypy - notice that no errors are reported - mypy
# understands that Person has a property named age so is happy
# with the function.

# Write a new function in the file that accepts a Person as a
# parameter and tries to access a property that doesn’t exist. Run
# it through mypy and check that it does report an error.


class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
print(eliza.address)


def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))



# New function: "is_engineer" takes "Person" as a parameter and tries to access "profession" - a property that does not exist.
def is_engineer(person: Person) -> bool:
    return person.profession == "Engineer"

print(is_engineer(eliza))

# After running through mypy, 2 errors related to the new function were reported:
# 1) exercise_five.py:36: error: Returning Any from function declared to return "bool"  [no-any-return]
# since person does not have "profession" as attribute and thus its type is unknown, thus this function could be returning any type. Hence the error above.
# 2) exercise_five.py:36: error: "Person" has no attribute "profession"  [attr-defined]
# The error above simply stating that attribute "profession" does not exist in the class "Person"


