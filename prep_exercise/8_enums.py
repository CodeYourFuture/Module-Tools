from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

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

# =====define parse age======
def parse_age(raw: str) -> int:
    try:
        age= int(raw)
    except ValueError:
        print("Error: age must be asn integer.", file=sys.stderr)
        sys.exit(1)

    if age <= 0:
        print("Error: age must be a positive integer.", file=sys.stderr)
        sys.exit(1)

    return age

# =====define parse operating system======
def parse_operating_system(raw: str) -> OperatingSystem:
    normalized = raw.strip().lower()

    aliases = {
        "macos": OperatingSystem.MACOS,
        "mac": OperatingSystem.MACOS,
        "arch": OperatingSystem.ARCH,
        "arch linux": OperatingSystem.ARCH,
        "ubuntu": OperatingSystem.UBUNTU,
    }

    if normalized not in aliases:
        valid = ", ".join(sorted(aliases.keys()))
        print(f"Error: invalid operating system. Try one of: {valid}", file=sys.stderr)
        sys.exit(1)

    return aliases[normalized]


# =======count laptops by os============
def count_laptops_by_os(laptops: List[Laptop]) -> Dict[OperatingSystem, int]:
    counts: Dict[OperatingSystem, int] = {os: 0 for os in OperatingSystem}
    for laptop in laptops:
        counts[laptop.operating_system] +=1
    return counts


# ======define main ================
def main() -> None:
    laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13.0, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15.0, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15.0, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13.0, operating_system=OperatingSystem.MACOS),
]

    name = input("Enter your name: ").strip()
    if not name:
        print("Error: name cannot be empty.", file=sys.stderr)
        sys.exit(1)

    age = parse_age(input("Enter your age: "))
    preferred_os = parse_operating_system(input("preferred OS(Ubuntu / Arch / macOS): "))

    person = Person(name=name, age=age, preferred_operating_system=preferred_os)

    counts = count_laptops_by_os(laptops)
    preferred_count = counts[person.preferred_operating_system]

    print(f"\nHi {person.name} (age {person.age})")
    print(f"Laptops available with {person.preferred_operating_system.value}: {preferred_count}")

    # Find the OS with maximum availability
    best_os = max(counts, key=lambda os:counts[os])
    best_count = counts[best_os]

    if best_os != person.preferred_operating_system and best_count > preferred_count:
        print(
            f"If you are willing to accept {best_os.value} instead,"
            f"You're more likely to get a laptop. {best_count} available."
        )

if __name__ == "__main__":
    main()
