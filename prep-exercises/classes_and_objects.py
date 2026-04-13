class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system


def is_adult(person: Person) -> bool:
    return person.age >= 18


imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
# print(imran.address)
# Person doesn't have address attribute

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
# print(eliza.address)
# Person doesn't have address attribute

# def favorite_song(person: Person) -> str:
#     return person.song
# error because person doesn't have song attribute
