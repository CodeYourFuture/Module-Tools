class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


def is_adult(person: Person) -> bool:
    return person.age >= 18

def print_email(person: Person) -> None:
    return person.email

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
#print(imran.address) doesnt worrk becuase there no address atribute

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
#print(eliza.address) doesnt worrk becuase there no address atribute

print(is_adult(imran))

#print(print_email(imran)) there is no email atribute to print