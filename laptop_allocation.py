from dataclasses import dataclass, field
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
    
    def __hash__(self):
        return hash((self.name, self.age))


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem
    
def allocate_laptops(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
    if len(people) > len(laptops):
        raise Exception("Sorry, there are not enough laptops.")
    alloc_dict = {}
    # people with fewer options choose first, because they potentially can generate most sadness
    people.sort(key=lambda person: len(person.preferred_operating_system))
    for person in people:
        for laptop in laptops:
            is_match = False
            # if it a last chance to get a laptop, it used anyway 
            if laptops.index(laptop) == len(laptops) - 1:
                alloc_dict[person] = laptop
                break
            for sys in person.preferred_operating_system:
                if sys == laptop.operating_system:
                    alloc_dict[person] = laptop
                    laptops.pop(laptops.index(laptop))
                    is_match = True
                    break
            if is_match:
                break
    return alloc_dict
    
def calcSadness(person: Person, laptop: Laptop) -> int:
    sadness = 0
    is_sys_matched = False
    for i in range(len(person.preferred_operating_system)):
        if person.preferred_operating_system[i] == laptop.operating_system:
            is_sys_matched = True
            sadness += i
            break
    if not is_sys_matched:
        sadness = 100
    return sadness

def print_allocation(alloc_dict: Dict[Person, Laptop]) -> None:
    for person in alloc_dict.keys():
        print(f"{person.name} gets: {alloc_dict[person].model} with {alloc_dict[person].operating_system.name}.")

def main() -> None:
    people_five = [
        Person(name="Alice", age=28, 
            preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person(name="Bob", age=34, 
            preferred_operating_system=[OperatingSystem.ARCH]),
        Person(name="Charlie", age=22, 
            preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
        Person( name="Dana", age=41, 
            preferred_operating_system=[OperatingSystem.MACOS]),
        Person(name="Eli", age=25, 
            preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.MACOS])
    ]
    laptops_five = [
        Laptop(id=1, manufacturer="Apple", model="MacBook Pro 14", screen_size_in_inches=14.2, operating_system=OperatingSystem.MACOS),
        Laptop(id=2, manufacturer="Framework", model="Laptop 13", screen_size_in_inches=13.5, operating_system=OperatingSystem.ARCH),
        Laptop(id=3, manufacturer="Dell", model="XPS 13 Developer Edition", screen_size_in_inches=13.4, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=4, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13.6, operating_system=OperatingSystem.MACOS),
        Laptop(id=5, manufacturer="Lenovo", model="ThinkPad X1 Carbon", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH)
    ]
    people_ten = [
        Person(name="Alice", age=28, 
            preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person(name="Bob", age=34, 
            preferred_operating_system=[OperatingSystem.ARCH]),
        Person(name="Charlie", age=22, 
            preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
        Person( name="Dana", age=41, 
            preferred_operating_system=[OperatingSystem.MACOS]),
        Person(name="Eli", age=25, 
            preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.MACOS]),
        Person(name="Fiona", age=30, 
            preferred_operating_system=[OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
        Person(name="George", age=27, 
            preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.ARCH]),
        Person(name="Hannah", age=29, 
            preferred_operating_system=[OperatingSystem.ARCH]),
        Person(name="Ian", age=38, 
            preferred_operating_system=[OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person(name="Julia", age=24, 
            preferred_operating_system=[OperatingSystem.ARCH, OperatingSystem.UBUNTU])
    ]
    laptops_ten = [
        Laptop(id=1, manufacturer="Apple", model="MacBook Pro 14", screen_size_in_inches=14.2, operating_system=OperatingSystem.MACOS),
        Laptop(id=2, manufacturer="Framework", model="Laptop 13", screen_size_in_inches=13.5, operating_system=OperatingSystem.ARCH),
        Laptop(id=3, manufacturer="Dell", model="XPS 13 Developer Edition", screen_size_in_inches=13.4, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=4, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13.6, operating_system=OperatingSystem.MACOS),
        Laptop(id=5, manufacturer="Lenovo", model="ThinkPad X1 Carbon", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH),
        Laptop(id=6, manufacturer="System76", model="Lemur Pro", screen_size_in_inches=14.1, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=7, manufacturer="Apple", model="MacBook Pro 16", screen_size_in_inches=16.2, operating_system=OperatingSystem.MACOS),
        Laptop(id=8, manufacturer="Razer", model="Blade 14", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH),
        Laptop(id=9, manufacturer="HP", model="Dev One", screen_size_in_inches=14.0, operating_system=OperatingSystem.UBUNTU),
        Laptop(id=10, manufacturer="ASUS", model="ROG Zephyrus G14", screen_size_in_inches=14.0, operating_system=OperatingSystem.ARCH)
    ]
    laptops_twenty = [
        Laptop(1, "Apple", "MacBook Pro 14", 14.2, OperatingSystem.MACOS),
        Laptop(2, "Framework", "Laptop 13", 13.5, OperatingSystem.ARCH),
        Laptop(3, "Dell", "XPS 13", 13.4, OperatingSystem.UBUNTU),
        Laptop(4, "Apple", "MacBook Air M3", 13.6, OperatingSystem.MACOS),
        Laptop(5, "Lenovo", "ThinkPad X1 Carbon", 14.0, OperatingSystem.ARCH),
        Laptop(6, "System76", "Lemur Pro", 14.1, OperatingSystem.UBUNTU),
        Laptop(7, "Apple", "MacBook Pro 16", 16.2, OperatingSystem.MACOS),
        Laptop(8, "Razer", "Blade 14", 14.0, OperatingSystem.ARCH),
        Laptop(9, "HP", "Dev One", 14.0, OperatingSystem.UBUNTU),
        Laptop(10, "ASUS", "ROG Zephyrus G14", 14.0, OperatingSystem.ARCH),
        Laptop(11, "Apple", "MacBook Air M2", 15.3, OperatingSystem.MACOS),
        Laptop(12, "Star Labs", "StarBook", 14.0, OperatingSystem.ARCH),
        Laptop(13, "Lenovo", "ThinkPad P16", 16.0, OperatingSystem.UBUNTU),
        Laptop(14, "Microsoft", "Surface Laptop (Linux Mod)", 13.5, OperatingSystem.ARCH),
        Laptop(15, "Apple", "MacBook Pro 13", 13.3, OperatingSystem.MACOS),
        Laptop(16, "Framework", "Laptop 16", 16.0, OperatingSystem.ARCH),
        Laptop(17, "Dell", "Precision 5570", 15.6, OperatingSystem.UBUNTU),
        Laptop(18, "System76", "Pangolin", 15.6, OperatingSystem.UBUNTU),
        Laptop(19, "Apple", "MacBook Air", 13.3, OperatingSystem.MACOS),
        Laptop(20, "Tuxedo", "InfinityBook Pro", 14.0, OperatingSystem.ARCH)
    ]
    people_twenty = [
        Person("Alice", 25, [OperatingSystem.ARCH]),
        Person("Bob", 32, [OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person("Charlie", 19, [OperatingSystem.ARCH, OperatingSystem.UBUNTU]),
        Person("Diana", 45, [OperatingSystem.MACOS]),
        Person("Edward", 28, [OperatingSystem.ARCH, OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person("Fiona", 31, [OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
        Person("George", 27, [OperatingSystem.ARCH]),
        Person("Hannah", 22, [OperatingSystem.MACOS, OperatingSystem.ARCH]),
        Person("Ian", 35, [OperatingSystem.MACOS]),
        Person("Julia", 29, [OperatingSystem.ARCH, OperatingSystem.MACOS]),
        Person("Kevin", 24, [OperatingSystem.ARCH]),
        Person("Laura", 33, [OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person("Mason", 26, [OperatingSystem.ARCH, OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
        Person("Nora", 40, [OperatingSystem.MACOS]),
        Person("Oliver", 21, [OperatingSystem.ARCH]),
        Person("Paige", 30, [OperatingSystem.UBUNTU]),
        Person("Quinn", 23, [OperatingSystem.ARCH, OperatingSystem.MACOS]),
        Person("Riley", 38, [OperatingSystem.MACOS, OperatingSystem.UBUNTU]),
        Person("Sam", 25, [OperatingSystem.ARCH]),
        Person("Tina", 29, [OperatingSystem.MACOS, OperatingSystem.ARCH])
    ]
    # inside allocation function .pop() function is used when laptop selected - 
    # so copy of original list is passed to avoid mutation
    result_dict_5 = allocate_laptops(people=people_five, laptops=laptops_five.copy())
    result_dict_10 = allocate_laptops(people=people_ten, laptops=laptops_ten.copy())
    result_dict_20 = allocate_laptops(people=people_twenty, laptops=laptops_twenty.copy())
    print("####################################result for 5 people and 5 laptops#####################################")
    print_allocation(alloc_dict=result_dict_5)
    sadness_5 = 0
    for person in result_dict_5.keys():
        sadness_5 += calcSadness(person, result_dict_5[person])
    print(f"Total sadness: {sadness_5}")
    print("###################################result for 10 people and 10 laptops####################################")
    print_allocation(alloc_dict=result_dict_10)
    sadness_10 = 0
    for person in result_dict_10.keys():
        sadness_10 += calcSadness(person, result_dict_10[person])
    print(f"Total sadness: {sadness_10}")
    print("###################################result for 20 people and 20 laptops####################################")
    print_allocation(alloc_dict=result_dict_20)
    sadness_20 = 0
    for person in result_dict_20.keys():
        sadness_20 += calcSadness(person, result_dict_20[person])
    print(f"Total sadness: {sadness_20}")

if __name__ == "__main__":
    main()