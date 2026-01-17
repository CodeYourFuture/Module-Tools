import argparse
import cowsay
import sys

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things"
)

parser.add_argument(
    "--animal",
    choices=cowsay.char_names,
    default="cow",
    help="The animal to be saying things."
)

parser.add_argument(
    "--list-animals",
    action="store_true",
    help="List available animals and exit."
)

parser.add_argument(
    "message",
    nargs="*",
    help="The message for the animal to say."
)

args = parser.parse_args()

if args.list_animals:
    print("\n".join(cowsay.char_names))
    sys.exit(0)

if not args.message:
    parser.error("the following arguments are required: message")

getattr(cowsay, args.animal)(" ".join(args.message))
