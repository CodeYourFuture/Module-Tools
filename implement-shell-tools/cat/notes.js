import process from "node:process";
import { promises as fs } from "node:fs";
// const fs = promises

// * `cat sample-files/1.txt`
// * `cat -n sample-files/1.txt`
// * `cat sample-files/*.txt`
// * `cat -n sample-files/*.txt`
// * `cat -b sample-files/3.txt`

//from coursework
// const content = await fs.readFile(path, "utf-8");
// const countOfWordsContainingEs = content
//   .split(" ")
//   .filter((word) => word.includes("e"))
//   .length;
// console.log(countOfWordsContainingEs);

// process.argv documentation that process.argv[0] will be the path to node
// process.argv[1] will be the path to this file
// the arguments start at index 2



// 1 `cat sample-files/1.txt`
// async function caseOne(oneFile) {
//     const content = await fs.readFile(file, "utf-8");
//     console.log(content);
// }
// 3 `cat sample-files/*.txt`
// async function caseThree(listOfFiles) {
//     for (const file of listOfFiles) {
//         const content = await fs.readFile(file, "utf-8");

//         console.log(content);
//   }
// }

