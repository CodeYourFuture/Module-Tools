import cowsay
import sys
import argparse

listed_animals = [listed_animal for listed_animal in dir(cowsay) if callable(getattr(cowsay, listed_animal)) and not listed_animal.startswith("__") and listed_animal not in ["draw", "func", "get_output_string", "CowsayError"]]

parser = argparse.ArgumentParser(
    prog="cow",
    description="Makes animals say things",
)

parser.add_argument("--animal", help="Select an animal to say anything", choices=listed_animals)
parser.add_argument("message", nargs ="+", help="The message that the animal says")

args = parser.parse_args()

message = " ".join(args.message)
animal = args.animal or "cow"


if animal not in listed_animals:
    print(f"Error: argument --animal: invalid choice: '{animal}'. Choose from: {', '.join(listed_animals)}")
    exit(1)

animal_says = getattr(cowsay, animal)

print(animal_says(message))

