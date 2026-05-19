import argparse
import cowsay


def main():
    # Get animals dynamically from cowsay (DO NOT hardcode)
    animals = cowsay.char_names

    parser = argparse.ArgumentParser(
        prog="cowsay",
        description="Make animals say things"
    )

    parser.add_argument(
        "--animal",
        choices=animals,
        default="cow",
        help="The animal to be saying things."
    )

    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say."
    )

    args = parser.parse_args()

    message = " ".join(args.message)

    print(cowsay.get_output_string(args.animal, message))


if __name__ == "__main__":
    main()