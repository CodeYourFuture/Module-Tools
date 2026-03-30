# This program lets you choose an animal (like a cow, dragon, etc.) to "say" a message using ASCII art.
# It uses command-line arguments to get the animal type and the message.
# The message is combined into a single string, and the correct cowsay function is called to display it.

import argparse
import cowsay

def parse_arguments():
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
        "message",
        nargs="+",
        help="The message to say."
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    message = " ".join(args.message)
    say_func = getattr(cowsay, args.animal)
    say_func(message)

if __name__ == "__main__":
    main()
