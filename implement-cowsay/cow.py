import cowsay
import argparse

def main():
    # Get dynamic list of animals from the cowsay library
    animals = cowsay.char_names

    parser = argparse.ArgumentParser(
        prog="cowsay",
        description="Make animals say things"
    )

    parser.add_argument("--animal", choices=animals, help="The animal to be saying things.")
    parser.add_argument("message", nargs="+", help="The message to say.")

    args = parser.parse_args()

    # Join all message words into a single string
    message = " ".join(args.message)

    if args.animal:
        cowsay.char_funcs[args.animal](message)
    else:
        cowsay.cow(message)

if __name__ == "__main__":
    main()
