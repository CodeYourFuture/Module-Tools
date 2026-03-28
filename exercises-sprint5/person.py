from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
    today_date = date.today().year
    birth_year = self.date_of_birth.year
    age = today_date - birth_year


    return age >= 18

imran = Person("Imran", date(2000, 6, 20), "Ubuntu")
print(imran.name)


eliza = Person("Eliza", date(1987, 12, 10), "Arch Linux")
print(eliza.name)



# when I ran mypy I got this errors:
# person.py:9: error: "Person" has no attribute "address"  [attr-defined]
# person.py:13: error: "Person" has no attribute "address"  [attr-defined]
# So I will remove .address line as mypy caught rightly that Person class does not have address property. It shows the benefit of using classes as earlier without defining a class mypy could not catch the same bug. 


#def get_address(person: Person) -> str:
    #return person.address

#print(is_adult(imran))
# When I ran mypy with is_adult function I got no error as age is a property of Person class 

# however when I added get_address function and ran mypy again I got this error: person.py:27: error: "Person" has no attribute "address"  [attr-defined]Found 1 error in 1 file (checked 1 source file) which was expected as Person class has no address attribute