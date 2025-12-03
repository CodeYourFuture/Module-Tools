from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_system: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system="macOS"),
] 
people = [
    Person(name="Imran", age=22, preferred_operating_system=["Arch Linux","Ubuntu"]),
    Person(name="Eliza", age=34, preferred_operating_system=["Arch Linux","macOS","Ubuntu"]),
    Person(name="Leila", age=45, preferred_operating_system=["macOS","Ubuntu","Arch Linux",]),    
   Person(name="Mary", age=35, preferred_operating_system=["macOS","Arch Linux"]),
]
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]: 
    for person in people :
     allocated=False
     for i in range(len(person.preferred_operating_system)) :
          for laptop in laptops :
              if person.preferred_operating_system[i] == laptop.operating_system :
                  print(person.name,laptop.id,laptop.operating_system,i)
                  laptops.remove(laptop)
                  allocated=True
                  break
          if allocated : break        
    
allocate_laptops(people,laptops)    
