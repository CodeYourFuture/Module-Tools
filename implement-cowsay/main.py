import argparse
import cowsay

all_animals= sorted(cowsay.char_names)

parser = argparse.ArgumentParser(
    prog = "cowsay",
    description= "Make animals say things"
)

parser.add_argument(
    "--animal",
    choices = all_animals,
    default = "cow",
    help = "What do you want animal to say "

)

parser.add_argument(
    "message",
    nargs="+",
    help = "The message to say"
)

args = parser.parse_args()

full_message = " ".join(args.message)

print(cowsay.get_output_string(args.animal, full_message))
