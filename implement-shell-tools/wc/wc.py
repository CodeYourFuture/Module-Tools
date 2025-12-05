# import { program } from "commander";
# import { promises as fs } from "node:fs";
# import process from "node:process";
# import { stat } from "node:fs/promises";

# program
#   .name("count-containing-lines-words-characters")
#   .description("Counts lines, words or characters in a file (or all files) inside a directory")
#   .option("-l, --line", "The number of lines in each file")
#   .option("-w, --word", "The number of words in each file")
#   .option("-c, --character", "The number of characters in each file")
#   .argument("<path...>", "The file path to process");

# program.parse();

# const argv = program.args;

# const options = program.opts();


# function counter(item) {
#   const lines = item.trim().split("\n").length;
#   const words = item.split(/\s+/).filter(Boolean).length;
#   const characters = item.length;
#   return { lines, words, characters };
# }

# let totalLines = 0;
# let totalWords = 0;
# let totalCharacters = 0;
# let fileCount = 0;

# for (const path of argv) {
#     const pathInfo = await stat(path);

# if (pathInfo.isFile()) {
#     const content = await fs.readFile(path, "utf-8");
#     const stats = counter(content);
#     if (options.line) {
#         console.log(`${stats.lines} ${path}`);
#     } else if (options.word) {
#         console.log(`${stats.words} ${path}`);
#     } else if (options.character) {
#         console.log(`${stats.characters} ${path}`);
#     } else {
#         console.log(`${stats.lines}       ${stats.words}       ${stats.characters} ${path}`);
#     }

#     totalLines += stats.lines;
#     totalWords += stats.words;
#     totalCharacters += stats.characters;
#     fileCount++;

# } else if (pathInfo.isDirectory()) {
#     const files = await fs.readdir(path);
#     for (const file of files) {
#         const filePath = `${path}/${file}`;
#         const fileContent = await fs.readFile(filePath, "utf-8");
#         const stats = counter(fileContent);

#         if (options.line) {
#             console.log(`${stats.lines} ${filePath}`);
#         } else if (options.word) {
#            console.log(`${stats.words} ${filePath}`); 
#         } else if (options.character) {
#           console.log(`${stats.characters} ${filePath}`);
#         } else {
#             console.log(`${stats.lines}       ${stats.words}    ${stats.characters} ${filePath}`);
#         }

#         totalLines += stats.lines;
#         totalWords += stats.words;
#         totalCharacters += stats.characters;
#         fileCount++;
#     }
# }

# }

# if (fileCount > 1) {
#     if (options.line) {
#         console.log(`${totalLines} total`);
#     } else if (options.word) {
#       console.log(`${totalWords} total`);
#     } else if (options.character) {
#        console.log(`${totalCharacters} total`); 
#     } else {
#        console.log(`${totalLines}       ${totalWords}       ${totalCharacters} total`); 
#     }
# }

import argparse

parser = argparse.ArgumentParser(
    prog="counter",
    description="Counts lines, words or characters in a file (or all files) inside a directory",
)

parser.add_argument("-l", "--line", dest="line", help="The number of lines in each file", action="store_true")
parser.add_argument("-w", "---word", dest="word", help="The number of words in each file", action="store_true")
parser.add_argument("-c", "--char", dest="char", help="The number of characters in each file")
parser.add_argument("paths", help="The file(s)/path(s) to read from", nargs="+")

args = parser.parse_args()

def counter(item):
    lines = len(item.strip().split("\n"))
    words = len(item.split())
    characters = len(item)
    return {"lines": lines, "words": words, "characters": characters}


total_lines = 0
total_words = 0
total_characters = 0
file_count = 0


for path in args.paths:
    with open(path, "r") as f:
        content = f.read()
    stats = counter(content)
    if args.line:
        print(f"{stats[lines]} {path}")
    elif args.word:
        print()
    elif args.char:
        print()
    else:
        print("")


