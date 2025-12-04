import cowsay
import argparse

animals = cowsay.char_names

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things"
)

parser.add_argument("-a", "--animal", choices=animals, help="The animal to be saying things.")
parser.add_argument("message", nargs="+", help="The message to say.")

args = parser.parse_args()

message = " ".join(args.message)

print(args)

if args.animal:
    # cowsay[args.animal](message)
    print(cowsay.get_output_string(args.animal, message))
    # print('hi')
else:
    # print(cowsay.get_output_string('cow', 'Hello World'))
    cowsay.cow(message) # if no animal is provided, use default



print(animals)

 