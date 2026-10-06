from dataclasses import dataclass
from enum import Enum

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"
    # They can add extra OSes if they want, but at least must have all the ones defined for the laptops

# They may update with their solution from task 13
@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: list[Laptop], person: Person) -> list[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


people = [
    Person(name="Imran", age=22, preferred_operating_system=OperatingSystem.UBUNTU),
    Person(name="Eliza", age=34, preferred_operating_system=OperatingSystem.ARCH),
]

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]
    
name = input("Enter your name: ")
while True: # Any kind of input validation and good ux is fine
    try:
        age = int(input("Enter your age: "))
        break
    except:
        print("please enter a number") # at a bare minimum it MUST print something meaningful if there was an error
while True:
    try:
        os_text = input("Enter your operating system: ").lower()
        if "ubuntu" in os_text:
            os = OperatingSystem.UBUNTU
            break
        elif "arch" in os_text:
            os = OperatingSystem.ARCH
            break
        elif "mac" in os_text:
            os = OperatingSystem.MACOS
            break
        else:
            raise "invalid os"
    except:
        print("please enter one of: ubuntu, macos, arch")

new_person = Person(name=name, age=age, preferred_operating_system=os)
people.append(new_person)

for person in people:
    possible_laptops = find_possible_laptops(laptops, person)
    print(f"Possible laptops for {person.name}: {possible_laptops}")

# TASK 14
# The above code currently handles operating systems as strings.
#
# Refactor the code to use enums for operating systems.
#
# Check with mypy and test it to ensure the program still works correctly.
#
# Use the `input` function
# https://docs.python.org/3/library/functions.html#input
# to read a person's name, age, and preferred operating system,
# then add them to the list of people.
#
# Make sure your implementation has a good user experience, and properly validates the inputs, mapping an OS to one of the enum values.
#
# If an operating system can't be matched at all, your script should handle it appropriately and not crash.
