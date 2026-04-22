# Personal stretch exercise - Review not required
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Person(ABC):
    first_name: str
    last_name: str

    @abstractmethod
    def get_full_name(self) -> str: ...

@dataclass
class Parent(Person):
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

@dataclass
class Child(Person):
    previous_last_names: list[str] = field(default_factory=list)
    
    def change_last_name(self, last_name: str) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name
    
    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"

person1 = Child("Jane", "Doe")
print(person1.get_full_name())
person1.change_last_name("Smith")
print(person1.get_full_name())

person2 = Parent("John", "Doe")
print(person2.get_full_name())
