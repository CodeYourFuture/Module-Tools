import cowsay
import argparse
import sys


parser = argparse.ArgumentParser(description="displays cowsay charactor with given arguments")
parser.add_argument('animal', type=str, help= 'please enter a valid animal')
parser.add_argument('message', type=str, help= 'please enter a message')
arg = parser.parse_args()

valid_animals = cowsay.char_names

if arg.animal in valid_animals:
     animal_func = getattr(cowsay, arg.animal)
     print(animal_func(arg.message))
    
else:
    print(f"Error: '{arg.animal}' is not a valid animal.")
    print("Valid animals are:", ", ".join(valid_animals))
    sys.exit(1)
