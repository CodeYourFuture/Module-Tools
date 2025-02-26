import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and print files",
)
parser.add_argument("-n", action="store_true", help="Number lines")
parser.add_argument("-b", action="store_true", help="Number non-blank lines")
parser.add_argument("paths", nargs="*", help="Paths to concatenate and print")
args = parser.parse_args()

def parseNumberMode():
    if args.b:
        return "non-blank"
    elif args.n:
        return "all"
    else:
        return "none"


def calculatePrefix(numberMode, nonBlankLineNumber, lineNumberIncludingBlanks, thisLineIsBlank):
    if numberMode == "none":
        return ""
    if numberMode == "all":
        lineNumber = lineNumberIncludingBlanks
    elif thisLineIsBlank:
        return ""
    else:
        lineNumber = nonBlankLineNumber
    return f"{lineNumber}".rjust(6, " ") + "  "

numberMode = parseNumberMode()

for path in args.paths:
    with open(path, "r") as f:
        content = f.read()
    lines = content.split("\n");
    nonBlankLineNumber = 1;
    for i, line in enumerate(lines):
        if i == len(lines) - 1 and line == "":
            break
        prefix = calculatePrefix(numberMode, nonBlankLineNumber, i + 1, line == "")
        print(f"{prefix}{line}");
        if line != "":
            nonBlankLineNumber += 1
