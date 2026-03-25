import { program } from "commander";
import process from "node:process";
import { promises as fs } from "node:fs";

program.name("wc").description("Print the number of lines, word and bytes for each file and a total if there are multiple files")
.option("-l, --lines", "Print the number of lines")
.option("-w, --words", "Print the number of words")
.option("-c, --bytes", "Print the number of bytes")
.argument("<path>", "The file path").allowExcessArguments()
program.parse()

const argv = program.args;


const stringArr = [];
for (const path of argv) {
    stringArr.push(await fs.readFile(path, "utf-8"));
}

const infoArr = [];
for (let i = 0; i < stringArr.length; i++) {
    const arr = [];
    const line = stringArr[i].split("\n")//.filter(e => e.includes("\n"))
    arr.push(line.length - 1)
    arr.push(stringArr[i].split(" ").flatMap(l => l.split("\n").map((l, i, a) => i < a.length - 1 ? l + "\n" : l).filter(l => l.trim() !== "")).length)
    arr.push(new Blob([stringArr[i]]).size)
    arr.push(argv[i])
    infoArr.push(arr.join(" "))
}

console.log(infoArr)