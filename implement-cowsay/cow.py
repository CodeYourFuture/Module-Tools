import argparse
import cowsay

def main():
    parser = argparse.ArgumentParser(description="Make animals say things")

    parser.add_argument(
        "--animal",
        choices=cowsay.char_names,
        default="cow",
        help="The animal to be saying things.",
    )

    parser.add_argument(
        "message",
        nargs="+",
        help="The message to say.",
    )

    args = parser.parse_args()

    text = " ".join(args.message)
    print(cowsay.get_output_string(args.animal, text))


if __name__ == "__main__":
    main()