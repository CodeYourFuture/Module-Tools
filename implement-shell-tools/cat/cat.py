import sys
import os


def main():
    args = sys.argv[1:]
    flags = []
    addresses = []
    for item in args:
        if item[0] == "-":
            flags.append(item)
        else:
            addresses.append(item)

    outputLines = []
    for fileAddress in addresses:
        try:
            lines = readFileByLines(fileAddress)
            for line in lines:
                outputLines.append(line)
        except Exception as e:
            print(e)
    printLines(outputLines, flags)


def readFileByLines(fileAddress):
    file = open(fileAddress, "r", encoding="utf-8")
    content = file.read()
    lines = content.split("\n")
    if len(lines) != 0 and lines[-1] == "":
        lines.pop()
    return lines


def printLines(outputLines, flags):
    lineNumber = 1
    for line in outputLines:
        if ("-n" in flags and "-b" not in flags) or ("-b" in flags and line != ""):
            output = "     " + str(lineNumber) + "  " + line
            print(output)
            lineNumber += 1
        else:
            print(line)


if __name__ == "__main__":
    main()
