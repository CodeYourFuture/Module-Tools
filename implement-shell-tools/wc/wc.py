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
    isLinesNumDisplay = "-l" in flags
    isWordsNumDisplay = "-w" in flags
    isBytesNumDisplay = "-c" in flags
    isNoFlags = len(flags) == 0
    totalLines = 0
    totalWords = 0
    totalBytes = 0
    for address in addresses:
        file = open(address)
        fileContent = file.read()
        linesNum = countFileLines(fileContent)
        wordsNum = countFileWords(fileContent)
        bytes = os.path.getsize(address)
        totalLines += linesNum
        totalWords += wordsNum
        totalBytes += bytes
        output = "  "
        if isLinesNumDisplay or isNoFlags:
            output += str(linesNum) + " "
        if isWordsNumDisplay or isNoFlags:
            output += str(wordsNum) + " "
        if isBytesNumDisplay or isNoFlags:
            output += str(bytes) + " "
        print(output + address)
    totalOutput = "  "
    if isLinesNumDisplay or isNoFlags:
        totalOutput += str(totalLines) + " "
    if isWordsNumDisplay or isNoFlags:
        totalOutput += str(totalWords) + " "
    if isBytesNumDisplay or isNoFlags:
        totalOutput += str(totalBytes) + " "
    print(totalOutput + "total")


def countFileLines(fileContent):
    lines = fileContent.split("\n")
    linesNum = len(lines)
    if lines[linesNum - 1] == "":
        linesNum -= 1
    return linesNum


def countFileWords(fileContent):
    fileContent = fileContent.replace("\n", " ")
    words = fileContent.split(" ")
    words = list(filter(lambda word: word != "", words))
    return len(words)


if __name__ == "__main__":
    main()
