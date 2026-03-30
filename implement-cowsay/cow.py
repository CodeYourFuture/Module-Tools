import cowsay
import argparse

# cowsay.cow(" ".join(sys.argv[1:]))

parser = argparse.ArgumentParser(
    prog="custom-cowsay",
    description="A custom cowsay can parse in animal in command line"
)

parser.add_argument("--animal", choices=cowsay.char_names, help="Parsing animal name after the flag")
parser.add_argument("message", nargs="+", help="Message for the animal to say")

args = parser.parse_args()

message = " ".join(args.message)

if (args.animal):
    print(cowsay.get_output_string(args.animal, message))
else:
    print(cowsay.get_output_string('cow', message))