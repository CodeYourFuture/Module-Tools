class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str,address:str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.address=address

amy = Person("Amy", 22, "Ubuntu", "23 main road")
print(amy.name)

eliza = Person("Eliza", 34, "Arch Linux","32 divert way")
print(eliza.name)

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(amy))

def home_address(person :Person):
    return person.address 

print(home_address(eliza))
