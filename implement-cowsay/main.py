#!/usr/bin/env python3

import cowsay
import argparse

animals = cowsay.char_names

parser = argparse.ArgumentParser(
    prog='cowsay',
    description='Make animals say things',
    epilog='Choose an animal and write a message'
)

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say."
    )

parser.add_argument(
    "--animal",
    choices=animals,
    default="cow",
    help="The animal must say something"
)

args = parser.parse_args()

msg = " ".join(args.message)
animal = args.animal

if animal in animals:
    output = getattr(cowsay, animal)
    output(msg)