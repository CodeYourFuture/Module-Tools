#!/usr/bin/env python3
import argparse
import cowsay
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Make animals say things"
    )
    parser.add_argument(
        "message", nargs="+", help="The message to say."
    )
    parser.add_argument(
        "--animal",
        default="cow",
        help="The animal to be saying things."
    )

    args = parser.parse_args()

    text = " ".join(args.message)
    animal = args.animal  

    supported_animals = [
        "beavis", "cheese", "cow", "daemon", "dragon", "fox",
        "ghostbusters", "kitty", "meow", "miki", "milk", "octopus",
        "pig", "stegosaurus", "stimpy", "trex", "turkey", "turtle", "tux"
    ]

    if animal not in supported_animals:
        print(f"usage: cowsay [-h] [--animal {{{','.join(supported_animals)}}}] message [message ...]")
        print(f"cowsay: error: argument --animal: invalid choice: '{animal}' (choose from {','.join(supported_animals)})")
        sys.exit(1)

    output = cowsay.get_output_string(animal, text)
    print(output)

if __name__ == "__main__":
    main()
