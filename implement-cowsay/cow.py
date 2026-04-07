import cowsay
import argparse

animals = cowsay.char_names;

parser = argparse.ArgumentParser(prog="cowsay", description="Make animals say things", usage="%(prog)s [-h] [--animal {" + ",".join(animals) + "}] message [message ...]")
parser.add_argument("--animal", help="{"+ ",".join(animals) +"} \nThe animal to be saying things.", default="cow")
parser.add_argument("message", help="The message to say.", nargs="+")

args = parser.parse_args()

if args.animal not in cowsay.char_names:
    parser.print_usage()
    print("cowsay: error: argument --animal: invalid choice: '" + args.animal + "' (choose from '" + "', '".join(animals) + "')")
else:
    print(cowsay.get_output_string(args.animal, " ".join(args.message[0:])))