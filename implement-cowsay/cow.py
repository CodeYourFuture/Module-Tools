#!/usr/bin/env python3
import argparse
import sys
import cowsay

def main():
    # Dynamically get available animals from the cowsay library
    animals = sorted(cowsay.char_names)

    parser = argparse.ArgumentParser(
        prog="cowsay",
        description="Make animals say things"
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
        help="The animal to be saying things."
    )

    args = parser.parse_args()
    msg = " ".join(args.message)

    # Render the chosen animal saying the message
    output = cowsay.get_output_string(args.animal, msg)
    sys.stdout.write(output + "\n")

if __name__ == "__main__":
    main()
