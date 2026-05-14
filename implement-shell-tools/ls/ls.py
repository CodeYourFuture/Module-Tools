import os
import sys
import argparse

def run_ls_command():
    parser = argparse.ArgumentParser()
    parser.add_argument("-1", "--one-per-line", action="store_true", dest="one")
    parser.add_argument("-a", "--all", action="store_true")
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()

    # ANSI Color Codes
    BLUE = '\033[34m'
    RESET = '\033[0m'

    try:
        # 1. Get and sort entries
        directory_entries = os.listdir(args.path)
        directory_entries.sort(key=str.lower)

        # 2. Filter out dotfiles unless -a is used
        visible_entries = []
        if args.all:
            visible_entries = directory_entries
        else:
            for name in directory_entries:
                if not name.startswith("."):
                    visible_entries.append(name)

        # 3. Apply colors to folders
        colored_entries = []
        for name in visible_entries:
            # We must join the path to the name to check if it's a folder correctly
            full_path = os.path.join(args.path, name)
            
            if os.path.isdir(full_path):
                # Wrap the name in Blue color codes
                colored_entries.append(f"{BLUE}{name}{RESET}")
            else:
                # Keep regular file name as is
                colored_entries.append(name)

        # 4. Build output string
        output_string = ""
        if args.one:
            output_string = "\n".join(colored_entries) + "\n"
        else:
            output_string = "  ".join(colored_entries) + "\n"

        if colored_entries:
            sys.stdout.write(output_string)

    except Exception as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_ls_command()