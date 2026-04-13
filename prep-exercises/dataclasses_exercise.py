from dataclasses import dataclass 
import datetime as dt

@dataclass(frozen=True)
class Person:
    name: str
    age: dt.date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = dt.datetime.today()

        age_in_year = today.year - self.age.year

        if (today.month, today.day) < (self.age.month, self.age.day):
            age_in_year -= 1
        return age_in_year >= 18

imran = Person("Imran", dt.date.fromisoformat("2002-08-05"), "Ubuntu")
print(imran)  

imran2 = Person("Imran", dt.date.fromisoformat("2002-08-05"), "Ubuntu")
print(imran == imran2) 

print(f'{imran.name} is adult: {imran.is_adult()}')
