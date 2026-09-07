class Person:
    def __init__(
        self,
        name: str,
        age: int,
        preferred_operating_system: str,
        address: str
    ):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.address = address
        
imran = Person("Imran",22,"Ubuntu","Sheffield")
print(imran.address)

#mypy knows what attributes a Person object is supposed to have. If you try to access an attribute that isn't defined in the class, mypy can warn you before you run the program.Adress needed to define in person object for print.