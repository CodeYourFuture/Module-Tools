import cowsay
import argparse   #helps you collect the words typed in command line 

def main():
    # Set up command-line parser
    parser = argparse.ArgumentParser(
        prog="cowsay",
        description="Make animals say things"
    )
    parser.add_argument(
        "--animal",
        choices=cowsay.char_names,   # fetch supported animals directly from cowsay
        default="cow",
        help="The animal chosen to be saying things"
    )
    parser.add_argument(
        "message",
        nargs="+",                   # accept one or more words as message 
        help="The message to say"
    )
    args = parser.parse_args()

    # Dynamically call the correct cowsay function
    say = getattr(cowsay, args.animal)
    say(" ".join(args.message))

if __name__ == "__main__":
    main()
