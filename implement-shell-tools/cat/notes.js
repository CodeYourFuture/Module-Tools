import process from "node:process";
import { promises as fs } from "node:fs";
// const fs = promises

// * `cat sample-files/1.txt`
// * `cat -n sample-files/1.txt`
// * `cat sample-files/*.txt`
// * `cat -n sample-files/*.txt`
// * `cat -b sample-files/3.txt`

// process.argv documentation that process.argv[0] will be the path to node
// process.argv[1] will be the path to this file
// the arguments start at index 2

const argv = process.argv.slice(2);
if (argv.length != 1) {
    console.error(`Expected exactly 1 argument (a path) to be passed but got ${argv.length}.`);
    process.exit(1);
}
const path = argv[0];

// const content = await fs.readFile(path, "utf-8");
// const countOfWordsContainingEs = content
//   .split(" ")
//   .filter((word) => word.includes("e"))
//   .length;
// console.log(countOfWordsContainingEs);

// `cat sample-files/1.txt`
const content = await fs.readFile('sample-files/1.txt', "utf-8");
const contentsOfFileOne = content
console.log(contentsOfFileOne);

// * `cat -n sample-files/1.txt`
const separatedToLines = content.split('\n')
separatedToLines.forEach((line, countLine) => {
    countLine+=1
    console.log(line, countLine})
const withAddedCount = countFileOne.

// * `cat sample-files/*.txt`

// * `cat -n sample-files/*.txt`

// * `cat -b sample-files/3.txt`

