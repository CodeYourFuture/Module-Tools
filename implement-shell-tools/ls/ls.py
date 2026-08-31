import argparse
import os

parser = argparse.ArgumentParser(prog="ls",
                                 description="simple ls clone")

parser.add_argument("-1",
                    dest="one_per_line",
                    action="store_true",
                    help="list one file per line")

parser.add_argument("-a",
                    dest="show_hidden_files",
                    action="store_true",
                    help="show hidden files")

parser.add_argument("filepath",
                    nargs="?",
                    default=".")

args = parser.parse_args()

entries = sorted(os.listdir(args.filepath))

if args.show_hidden_files:
    entries = [".", ".."] + entries
else:
    entries = [entry for entry in entries if not entry.startswith(".")]

if args.one_per_line:
    for entry in entries:
        print(entry)
else:
    joined = "\t".join(entries)
    print(joined)
