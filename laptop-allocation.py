from enum import Enum
from typing import List,Dict
from dataclasses import dataclass

from itertools import permutations
import sys

class OperatingSystem(Enum):
    UBUNTU = "ubuntu"
    MACOS="makos"
    ARCH = "arch linux"

@dataclass (frozen=True)
class Person:
    name:str
    age:int
    preferred_operating_system:List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

def sadness(person:Person,operating_system:OperatingSystem)->int:
    sad:int =100
    for index, os in enumerate(person.preferred_operating_system):
        if(os==operating_system):
            sad=index
            return sad

    return sad

def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    how_many_people= len(people)
    how_many_laptops = len(laptops)
    matrix = [[0 for i in range(how_many_laptops)] for _ in range(how_many_people)]
    for i, person in enumerate(people):
        for j,laptop in enumerate(laptops):
            matrix[i][j] = sadness(person,laptop.operating_system)
    print(matrix)

    best_prem = None
    min_sadness=100000000000
    for perm in permutations(range(how_many_laptops)):
      print(perm,"dsadsadsadsa")
      total =0
      for i in range(how_many_people):
        
        total+= matrix[i][perm[i]]
        
      print(total)
      if total< min_sadness :
            min_sadness = total
            best_perm = perm
            print(min_sadness,"minnnnnn")
            print(best_perm,"bestttt")

    print("=================================")
    print (best_perm,min_sadness)        


         
      


people = [
    Person(
        name="Imran",
        age=22,
        preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.ARCH,OperatingSystem.MACOS],
    ),
    Person(
        name="Eliza",
        age=34,
        preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.ARCH],
    ),
    Person(
        name="Eliza",
        age=34,
        preferred_operating_system=[OperatingSystem.MACOS],
    ),

]
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.MACOS),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    
]

allocate_laptops(people,laptops)      