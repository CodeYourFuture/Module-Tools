#Write a program which:

#1.Already has a list of Laptops that a library has to lend out.
#2.Accepts user input to create a new Person - it should use the input function to read a person’s
#name, age, and preferred operating system.
#3.Tells the user how many laptops the library has that have that operating system.
#4.If there is an operating system that has more laptops available, tells the user that if they’re willing to
#accept that operating system they’re more likely to get a laptop.

#You should convert the age and preferred operating system input from the user into more constrained
#types as quickly as possible, and should output errors to stderr and terminate the program with a non-
#zero exit code if the user input bad values.

from dataclasses import dataclass
import sys
from enum import Enum

class operatingSystem(Enum):
    CHROMEOS = "ChromeOS"
    WINDOWS = "Windows"
    MACOS = "macOS"
    LINUX = "Linux"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"



@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: str


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: operatingSystem



laptops = [
    Laptop(id=1, manufacturer="HP", model="Chromebook Plus 514", screen_size_in_inches=14, operating_system=operatingSystem.CHROMEOS),
    Laptop(id=2, manufacturer="Microsoft", model="XPS", screen_size_in_inches=13.8, operating_system=operatingSystem.WINDOWS),
    Laptop(id=3, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=15, operating_system=operatingSystem.MACOS),
    Laptop(id=4, manufacturer="Lenovo", model="ThinkPad X220", screen_size_in_inches=12.5, operating_system=operatingSystem.LINUX),
    Laptop(id=5, manufacturer="Dell", model="XPS", screen_size_in_inches=13.7, operating_system=operatingSystem.ARCH),
    Laptop(id=6, manufacturer="Dell", model="XPS", screen_size_in_inches=10.4, operating_system=operatingSystem.ARCH),
    Laptop(id=7, manufacturer="Dell", model="XPS", screen_size_in_inches=15.5, operating_system=operatingSystem.UBUNTU),
    Laptop(id=8, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=operatingSystem.UBUNTU),
    Laptop(id=9, manufacturer="Apple", model="MacBook", screen_size_in_inches=13.3, operating_system=operatingSystem.MACOS),
]


name_input = input("What's your name? ")
if not name_input.isalpha():
    print("Name must contain letters only!")
    sys.exit(1)

try:
    age_input = int(input("What's your age? "))
except ValueError:
    print("Enter a numeric value for the age!")
    sys.exit(1)


def parse_os_input(user_input: str) -> operatingSystem:
    clean = user_input.lower().replace(" ", "")
    
    for os in operatingSystem:
        if os.value.lower().replace(" ", "") == clean:
            return os
    print("Invalid operating system!", file=sys.stderr)
    sys.exit(1)

preferred_operating_system_input = parse_os_input(input("What's your preferred operating system? "))



def person_builder(name_input: str, age_input:int, preferred_operating_system_input:str) ->Person:

    return Person(name_input, age_input, preferred_operating_system_input)



def laptops_counter(preferred_operating_system_input:str) ->int:
    sum = 0
    for laptop in laptops:
        if preferred_operating_system_input == laptop.operating_system:
            sum += 1
    user_os = preferred_operating_system_input.value
    if sum == 1:
        return f"There is {sum} laptop with {user_os} operating system"
    elif sum > 1:
         return f"There are {sum} laptops with {user_os} operating system"

print(laptops_counter(preferred_operating_system_input))




def more_available_os(user_os: operatingSystem) ->int:
    os_counter = {}
    for laptop in laptops:
        os_counter[laptop.operating_system] = os_counter.get(laptop.operating_system, 0) + 1

    max_count = max(os_counts.values())

    user_os_count = os_counts.get(user_os, 0)
    
    if user_os_count < max_count:
        print(f"If you’re open to using {user_os} operating system, you’ll have a better chance of getting a laptop.”")


