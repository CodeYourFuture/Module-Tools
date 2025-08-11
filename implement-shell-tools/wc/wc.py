import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description="Count lines, words, and bytes in files (like wc)")
    parser.add_argument("-l", action="store_true", help="count lines")
    parser.add_argument("-w", action="store_true", help="count words")
    parser.add_argument("-c", action="store_true", help="count bytes")
    parser.add_argument("files", nargs="+", help="files to read")
    options = parser.parse_args()

if __name__ == "__main__":
    main()
