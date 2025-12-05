import sys
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    # Sorted in order of preference, most preferred is first.
    preferred_operating_systems: List[OperatingSystem]


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# In the prep, there was an exercise around finding possible laptops for a group of people.

# Your exercise is to extend this to actually allocate laptops to the people.
# Every person should be allocated exactly one laptop.

# If we define “sadness” as the number of places down in someone’s ranking the operating system the ended
# up with (i.e. if your preferences were [UBUNTU, ARCH, MACOS] and you were allocated a MACOS 
# machine your sadness would be 2), we want to minimise the total sadness of all people. 
# If we allocate someone a laptop with an operating system not in their preferred list, 
# treat them as having a sadness of 100.

laptops_list: List[Laptop] = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Lenovo", model="ThinkPad", screen_size_in_inches=14, operating_system=OperatingSystem.ARCH),
    Laptop(id=7, manufacturer="Asus", model="ZenBook", screen_size_in_inches=13, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=8, manufacturer="HP", model="Spectre", screen_size_in_inches=14, operating_system=OperatingSystem.MACOS),
    Laptop(id=9, manufacturer="Apple", model="MacBook Pro", screen_size_in_inches=16, operating_system=OperatingSystem.MACOS),
]

people: List[Person] = [
    Person(name="Imran", age=18, preferred_operating_systems=[OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    Person(name="Eliza", age=34, preferred_operating_systems=[OperatingSystem.ARCH, OperatingSystem.MACOS]),
    Person(name="Luke", age=26, preferred_operating_systems=[OperatingSystem.MACOS, OperatingSystem.UBUNTU, OperatingSystem.ARCH]),
    Person(name="Abby", age=30, preferred_operating_systems=[OperatingSystem.MACOS]),
    Person(name="Ger", age=51, preferred_operating_systems=[OperatingSystem.UBUNTU, OperatingSystem.MACOS]),
]

def user_prompt() -> Person:
    try:
        # strip() whitespace before processing (no need for str type here as input always returns a string)
        name = input("Please enter your first name: ").strip()
        if not name.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")

        # strip() before converting to integer
        age = int(input("Please enter your age: ").strip())
        minimum_age = 18
        if age < minimum_age: 
            raise ValueError("Age must be 18 or over.")


        # define valid OS options
        valid_os = [os.value for os in OperatingSystem]

        # prompt the user to enter OS preferences in order of preference (no need for str type here)
        preferred_os = input(f"Please enter your preferred operating systems in order of preference, separated by commas (e.g., {', '.join(valid_os)}): ").strip()

        # split and validate the OS
        preferred_os_list = [os.strip() for os in preferred_os.split(",")]
        preferred_os_enum = []
        for os_name in preferred_os_list:
            if os_name not in valid_os:
                raise ValueError(f"Invalid operating system: {os_name}")
        # convert to enum
            preferred_os_enum.append(OperatingSystem(os_name))

        return Person(name=name, age=age, preferred_operating_systems=preferred_os_enum)

    # throw an error and exit for invalid age and os input
    except ValueError as error:
        print(f"Invalid input: {error}", file=sys.stderr)
        sys.exit(1)


def find_possible_laptops(available_laptops: List[Laptop], current_person: Person) -> List[Laptop]:
    return [
        laptop for laptop in available_laptops
        if laptop.operating_system in current_person.preferred_operating_systems
    ]

# allocated sequentially, in a first come first served order
def allocate_laptops_sequentially(people: List[Person], laptops: List[Laptop]) -> Dict[Person, Laptop]:
   """
    Allocate laptops to people sequentially based on the order in the people list.
    This approach respects the 'wait your turn' principle.
    """