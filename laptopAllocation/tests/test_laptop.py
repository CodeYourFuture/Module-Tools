# test_basic.py
# A very small test just to confirm the core logic works.
# Full testing is beyond the scope of this assignment, but this shows
# that the sadness function behaves correctly for a simple case.
#If a person gets a laptop with their first‑choice operating system, their sadness should be 0.
from laptop import Person, Laptop, OperatingSystem, sadness

def test_sadness_first_choice():
    person = Person("Test", 20, (OperatingSystem.MACOS,))
    laptop = Laptop(1, "Apple", "macBook", 13, OperatingSystem.MACOS)

    assert sadness(person, laptop) == 0
