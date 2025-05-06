import argparse
import os

def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="custom_ls",
        description="Lists contents of a directory"
    )
    parser.add_argument(
        "path", nargs="?", default=".",
        help="Path to the target directory (defaults to current)"
    )
    parser.add_argument(
        "-1", dest="linewise", action="store_true",
        help="Display one entry per line"
    )
    parser.add_argument(
        "-a", dest="include_hidden", action="store_true",
        help="Include hidden files in the output"
    )
    return parser.parse_args()

def list_directory(path, show_hidden, one_per_line):
    try:
        items = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
        return
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
        return

    entries = [
        entry for entry in sorted(items)
        if show_hidden or not entry.startswith(".")
    ]

    if one_per_line:
        for entry in entries:
            print(entry)
    else:
        print("  ".join(entries))

def main():
    args = setup_arguments()
    list_directory(
        path=args.path,
        show_hidden=args.include_hidden,
        one_per_line=args.linewise
    )

if __name__ == "__main__":
    main()
