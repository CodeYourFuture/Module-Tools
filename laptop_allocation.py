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
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
] 
people = [
    Person(name="Imran", age=22, preferred_operating_system=[OperatingSystem.ARCH,OperatingSystem.UBUNTU]),
    Person(name="Eliza", age=34, preferred_operating_system=[OperatingSystem.ARCH,OperatingSystem.MACOS,OperatingSystem.UBUNTU]),
    Person(name="Leila", age=45, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.UBUNTU,OperatingSystem.ARCH]),    
    Person(name="Mary", age=35, preferred_operating_system=[OperatingSystem.MACOS,OperatingSystem.ARCH]),
    Person(name="Sara", age=28, preferred_operating_system=[OperatingSystem.MACOS])
]
sadness=0
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]: 
    sorted_people_OS_count=sorted(people,key=lambda p:len(p.preferred_operating_system))
    allocated_history : Dict[Person,Laptop] ={}
    global sadness
    for person in sorted_people_OS_count :
     allocated_flag=False
     for i in range(len(person.preferred_operating_system)) :
          for laptop in laptops :
              if person.preferred_operating_system[i] == laptop.operating_system :
                  allocated_history[person.name]=laptop
                #   print(person.name,laptop.id,laptop.operating_system,i)
                  sadness += i
                  laptops.remove(laptop)
                  allocated_flag=True
                  break
          if allocated_flag : 
            break     
          
     if not allocated_flag :
        allocated_history[person.name]=laptops[0]
        laptops.remove(laptops[0])
        sadness +=100       
              
    return allocated_history          

def print_final_allocation(allocated_history:dict[Person,Laptop]) :
    for name , laptop in allocated_history.items() :
        print(f"{name:<10} : Laptop Id {laptop.id:<3} - OS({laptop.operating_system}) ")
    print(f"Total sadness is : {sadness}")

print_final_allocation(allocate_laptops(people,laptops))