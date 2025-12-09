"""
Laptop Library System
This program helps library users find available laptops matching their
preferred operating system. It demonstrates enum usage, type safety,
and input validation.
"""


from dataclasses import dataclass
from enum import Enum
from typing import List
import sys


# --------------------------------------------------------------------
# ENUM DEFINITIONS
# --------------------------------------------------------------------
"""
    Represents valid operating systems for laptops.
    Using enums prevents string comparison issues (case, typos, spaces).
"""

class OperatingSystem(Enum):
    UBUNTU = "Ubuntu"
    MACOS = "macOS"
    ARCH = "Arch Linux"

# --------------------------------------------------------------------
# DATA CLASSES
# --------------------------------------------------------------------
#Represents a library user with their preferences.

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_systems: OperatingSystem


#Represents a laptop available in the library.
@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

# --------------------------------------------------------------------
# BUSINESS LOGIC
# --------------------------------------------------------------------
"""
    Filters laptops to find those matching the user's preferred OS.
    
    Args:
        laptops: List of available laptops
        person: User with OS preference
        
    Returns:
        List of laptops matching the user's preferred OS
"""
def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_systems:
            possible_laptops.append(laptop)
    return possible_laptops


# --------------------------------------------------------------------
# MAIN PROGRAM - USER INPUT AND PROCESSING
# --------------------------------------------------------------------
# Get user input as strings first (raw input)
name = input("Enter your name: ")
age_str = input("Enter your age: ")
os_str = input("Enter preferred OS: ")

# --------------------------------------------------------------------
# INPUT VALIDATION AND CONVERSION
# --------------------------------------------------------------------

# Convert age from string to integer with error handling
# Output to stderr as per requirements, exit with non-zero code
try:
    age = int(age_str)
except ValueError:
         
        print(f"Error: {age_str} is not a valid age", file=sys.stderr)
        sys.exit(1)

# Convert OS string to enum with error handling
try:
    os = OperatingSystem(os_str) 
except ValueError:
    print(f"Error: '{os_str}' is not a valid OS. Choose: Ubuntu, macOS, Arch Linux", file=sys.stderr)
    sys.exit(1)


# Create Person object from validated input
# Now we know age is a valid int and os is a valid OperatingSystem
person = Person(name=name, age=age,  preferred_operating_systems=os)

# --------------------------------------------------------------------
# DATA - AVAILABLE LAPTOPS
# --------------------------------------------------------------------
# Pre-defined list of laptops in the library (as per exercise requirements)
laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]


# --------------------------------------------------------------------
# PROCESSING - FIND MATCHING LAPTOPS
# --------------------------------------------------------------------
# Find laptops matching user's preferred OS
possible_laptops = find_possible_laptops(laptops, person)

# Requirement: Tell user how many laptops have their OS
print(f"we have {len(possible_laptops)} laptops with {os.value}")


# --------------------------------------------------------------------
# COUNTING LAPTOPS PER OPERATING SYSTEM
# --------------------------------------------------------------------
# Count laptops for each OS to find which has most
arch_count = 0
ubuntu_count = 0
macos_count = 0
for laptop in laptops:
    if laptop.operating_system == OperatingSystem.ARCH:
        arch_count += 1
    elif laptop.operating_system == OperatingSystem.UBUNTU:
        ubuntu_count += 1
    else:
        macos_count += 1




# --------------------------------------------------------------------
# FINDING THE OPERATING SYSTEM WITH MOST LAPTOPS
# --------------------------------------------------------------------
# Store counts in dictionary for easy max calculation
os_counts = {
    OperatingSystem.ARCH: arch_count,
    OperatingSystem.UBUNTU: ubuntu_count,
    OperatingSystem.MACOS: macos_count
}

# Find OS with maximum laptops
max_os = max(os_counts, key=os_counts.get)  # Gets the OS with highest count
max_count = os_counts[max_os]  # The actual count


# --------------------------------------------------------------------
# COMPARISON AND SUGGESTION LOGIC
# --------------------------------------------------------------------
# Get user's OS choice and count
os_user= person.preferred_operating_systems
user_count = os_counts[os_user]



# Requirement: Suggest alternative if another OS has MORE laptops
# Check: 1) Different OS, AND 2) Has strictly more laptops (> not >=)
if os_user != max_os and max_count > user_count:
    print(f" if you're willing to accept {max_os.value} " +
          f"you'd have {max_count} laptops available " + 
          f"(vs {user_count} for {os_user.value})")



