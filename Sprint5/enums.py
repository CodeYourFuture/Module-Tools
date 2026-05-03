import sys
from dataclasses import dataclass
from enum import Enum
from typing import List

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Laptop:
    id: int
    operating_system: OperatingSystem

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

laptops = [
    Laptop(id=1, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, operating_system=OperatingSystem.UBUNTU),
]

def get_user_person() -> Person:
    name = input("Enter your name: ")
    
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Error: Age must be a number.", file=sys.stderr)
        sys.exit(1)

    os_input = input("Enter preferred OS (macOS, Arch Linux, Ubuntu): ")
    try:
        pref_os = OperatingSystem(os_input)
    except ValueError:
        print(f"Error: '{os_input}' is not a valid operating system.", file=sys.stderr)
        sys.exit(1)
    return Person(name=name, age=age, preferred_operating_system=pref_os)

def main():
    user = get_user_person()
    counts = {os: 0 for os in OperatingSystem}
    for laptop in laptops:
        counts[laptop.operating_system] += 1

    user_pref = user.preferred_operating_system
    pref_count = counts[user_pref]
    print(f"There are {pref_count} laptops available with {user_pref.value}.")

    best_os = max(counts, key=counts.get)
    max_count = counts[best_os]

    if max_count > pref_count:
        print(f"Note: If you are willing to use {best_os.value}, we have {max_count} available. "
              "You're more likely to get one!")

if __name__ == "__main__":
    main()