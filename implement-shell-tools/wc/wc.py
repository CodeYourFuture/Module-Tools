import argparse

def setup_arguments():
    parser = argparse.ArgumentParser(
        prog="wordcount",
        description="A simple wc clone that reads files and displays line, word, and character counts."
    )

    parser.add_argument("files", nargs='+', help="Files to analyze")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-c", "--chars", action="store_true", help="Count characters")
    
    return parser.parse_args()

def read_text_from_file(path):
    with open(path, "r") as f:
        return f.read()

def count_lines(text):
    return len(text.rstrip('\n').split('\n'))

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def analyze_file(path):
    data = read_text_from_file(path)
    return {
        "lines": count_lines(data),
        "words": count_words(data),
        "chars": count_characters(data)
    }

def show_counts(counts, path, opts):
    if opts.lines:
        print(counts["lines"], path)
    elif opts.words:
        print(counts["words"], path)
    elif opts.chars:
        print(counts["chars"], path)
    else:
        print(counts["lines"], counts["words"], counts["chars"], path)

def show_total(all_counts, opts):
    total = {
        "lines": sum(c["lines"] for c in all_counts),
        "words": sum(c["words"] for c in all_counts),
        "chars": sum(c["chars"] for c in all_counts)
    }
    if opts.lines:
        print(total["lines"], "total")
    elif opts.words:
        print(total["words"], "total")
    elif opts.chars:
        print(total["chars"], "total")
    else:
        print(total["lines"], total["words"], total["chars"], "total")

def main():
    options = setup_arguments()
    all_results = []

    for file in options.files:
        result = analyze_file(file)
        all_results.append(result)
        show_counts(result, file, options)

    if len(options.files) > 1:
        show_total(all_results, options)

if __name__ == "__main__":
    main()
