import cowsay
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--animal", default="cow", choices=cowsay.char_names)
parser.add_argument("message", nargs="+")

args = parser.parse_args()
message = " ".join(args.message)

# getting list of animals names from the cowsay library, using (char_names);
animals = cowsay.char_names

for animal in animals:
    if args.animal == animal:
        print(cowsay.get_output_string(animal, message))
        break
