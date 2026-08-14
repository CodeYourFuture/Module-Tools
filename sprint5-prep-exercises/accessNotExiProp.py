class Person:
    def __init__(self, name: str):
        self.name = name

def get_name(person: Person) -> str:
    return person.name

def get_age(person: Person) -> int:
    return person.age
# As I expected, mypy prints an error saying that Person has no attribute name,
#  because the age property does not exist in the Person class.