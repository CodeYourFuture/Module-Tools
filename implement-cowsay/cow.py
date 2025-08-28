import cowsay
import argparse

# give a list of supported animal from cowsay 
list_of_choices = cowsay.char_names 


# to set argument parser
parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things",
)

# to pass optional flag with restricted choice :--animal
parser.add_argument(
    "--animal",
    choices=list_of_choices,
    default="cow",
    help="The animal to be saying things."
)

#  to add positional argument
parser.add_argument(
    "message", 
    nargs="*", 
    default="", 
    help="message to say") 

# To parse command line input
args = parser.parse_args()

message_text = " ".join(args.message)

# to print the result with selected element
print(cowsay.get_output_string(str(args.animal), message_text))

