import cowsay
import sys
import argparse

parser = argparse.ArgumentParser(
    prog="cow";
    description="Makes animals say things";
)

parser.add_argument("--animal", help="Select an animal to say anything")
parser.add_argument("message", nargs ="+" help="The message that the animal says")

args = parser.parse_args()