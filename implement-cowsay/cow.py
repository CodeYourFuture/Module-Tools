import argparse
import cowsay


parser = argparse.ArgumentParser(description="implement Cowsay command")
parser.add_argument("text", help="Text to be displayed")
parser.add_argument("--animal", help="Animal to say the text", default="cow")
args = parser.parse_args()

animals = cowsay.char_names
animal = args.animal.lower()
if animal not in animals:
    print(f"Invalid animal. Supported animals are: {', '.join(animals)}")
    exit(1)
cowsay.char_funcs[animal](args.text)    


