import cowsay
import argparse

parser = argparse.ArgumentParser(
    prog="Display items",
    description="Display the contents of a file reminiscent of the cat command"
)

parser.add_argument("--animal", help="Gives the user the option of adding the animal")
parser.add_argument("message", nargs="+", help="The message the animal needs to say.")

args = parser.parse_args()

animal_entered = args.animal
message_to_say = " ".join(args.message)

animals = [animal for animal in dir(cowsay) if callable(getattr(cowsay, animal))]

if animal_entered in animals:
    getattr(cowsay, animal_entered)(message_to_say)
else:
    print(f"'{animal_entered}' is not a valid animal. please choose from '{animals[1:]}'")
    print(f"Try one of: {', '.join(animals)}")
