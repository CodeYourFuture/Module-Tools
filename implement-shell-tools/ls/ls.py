# import process from "node:process";
# import { promises as fs } from "node:fs";
# import { program } from "commander";

# program
#   .name("list-files-in-directory")
#   .description("List all files and directories in a directory")
#   .argument("<path>", "The file path to process")
#   .option("-1, --one", "Output one entry per line")
#   .option("-a", "List all files & directories, including hidden ones");

# program.parse();

# const path = program.args[0];

# const options = program.opts();

# const directoryContent = await fs.readdir(path);

# let allContent = directoryContent;

# if (!options.a) {
#     allContent = directoryContent.filter(name => !name.startsWith("."));
# }

# for (const item of allContent) {
#     if (options.one) {
#         process.stdout.write(item + "\n");
#     } else {
#         process.stdout.write(item + "  ");
#     }
#     }

import argparse
import os

parser = argparse.ArgumentParser(
    prog="list-files-in-directory",
    description="List all files and directories in a directory",
)

parser.add_argument("-1", help="Output one entry per line", action="store_true")
parser.add_argument("-a", "--one", help="List all files & directories, including hidden ones", action="store_true")
parser.add_argument("path", help="The file path to read from")

args = parser.parse_args()

content = os.listdir(args.path)






    
