import cowsay
import argparse   #helps you collect the words typed in command line 

parser = argparse.ArgumentParser(prog="cowsay", description ="Make Animals say things")
parser.add_argument(
    "--animal",
    choices = (cowsay.char_names),
    help = "The animal chosen to be saying things",
    default = "cow"
    )
parser.add_argument(
    "message",
    nargs="+", #tells argparse that this argument can accept one or more values and collect them into a list.
    help="The message to say."
)
args = parser.parse_args()

getattr(cowsay, args.animal)(" ".join(args.message)) #Python built‑in func that get an attribute from an object by name = cowsay module in our case.



#we now need to fetch animals from cowsay.char_names
print(cowsay.char_names)