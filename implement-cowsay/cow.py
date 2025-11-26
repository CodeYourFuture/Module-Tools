import cowsay
import sys
import argparse

parser=argparse.ArgumentParser(prog="cowsay",
                               description="Make animals say things.")
parser.add_argument("message",nargs="+",help="The message to say.")
valid_animals=cowsay.char_names;
parser.add_argument("--animal",
                    choices=valid_animals,
                    help=" The animal to be saying things.",
                    default="cow")

args=parser.parse_args();
getattr(cowsay,args.animal)(" ".join(args.message))

       