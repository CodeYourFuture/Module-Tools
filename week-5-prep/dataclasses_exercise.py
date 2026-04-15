from dataclasses import dataclass
import datetime as dt

@dataclass(frozen=True)
class Person:
    name: str
    age: dt.date
    preferred_operating_system: str

imran = Person("Imran", "2004-04-18", "Ubuntu")
print(imran)

imran2 = Person("Imran", "2004-04-18", "Ubuntu")
print(imran == imran2)