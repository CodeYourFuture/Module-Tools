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


@dataclass(frozen=True)
class person:
    name: str
    age: int
    preferred_operating_system: str


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: str


laptops = [
    Laptop(id=1, manufacturer="HP", model="Chromebook Plus 514", screen_size_in_inches=14, operating_system="ChromeOS"),
    Laptop(id=2, manufacturer="Microsoft", model="XPS", screen_size_in_inches=13, operating_system="Windows"),
    Laptop(id=3, manufacturer="Apple", model="MacBook Air", screen_size_in_inches=15, operating_system="macOS"),
    Laptop(id=4, manufacturer="Lenovo", model="ThinkPad X220", screen_size_in_inches=12, operating_system="Linux"),
    Laptop(id=5, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system="Arch Linux"),
    Laptop(id=6, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="Ubuntu"),
    Laptop(id=7, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system="ubuntu"),
    Laptop(id=8, manufacturer="Apple", model="MacBook", screen_size_in_inches=13, operating_system="macOS"),
]