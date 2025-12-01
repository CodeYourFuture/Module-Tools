# import process from "node:process";
# import {promises as fs} from "node:fs";
# import {program} from "commander";

# program
#     .name("display-file-content")
#     .description("Output the content of a file to the terminal")
#     .argument("<path...>", "The file path to process")
#     .option("-n", "Number the output lines")
#     .option("-b","Number the non-blank output lines")

# program.parse();

# const paths = program.args;

# const options = program.opts();

# let lineNumber = 1;

# for (const path of paths) {
#     const filesContent = await fs.readFile(path, "utf-8");

#     const lines = filesContent.split("\n");

#     if (lines[lines.length - 1] === "") {
#         lines.pop();
#     }

#     for (let line of lines) {
#     if (options.n) {
#         process.stdout.write(`${lineNumber}  ${line}\n`);
#         lineNumber++;
#     } else if (options.b) {
#         if (line != "") {
#         process.stdout.write(`${lineNumber}  ${line}\n`);
#         lineNumber++;
#         } else {
#         process.stdout.write("\n");
#         }
#     } else {
#         process.stdout.write(line + "\n");
#     }
#     }
# }

import argparse

parser = argparse.ArgumentParser(
    prog="display-file-content",
    description="Output the content of a file to the terminal",
)

parser.add_argument("-n", help="Number the output lines")
parser.add_argument("-b", help="Number the non-blank output lines")
parser.add_argument("path", help="The file to read from")

args = parser.parse_args()

with open(args.path, "r") as f:
    content = f.read()


print(f)



