import { promises as fs } from "node:fs";
import process from "node:process";
// const path = require("node:path");
import path from "node:path";
const pathToFile = process.argv[1];
// console.log(pathToFile);
const formattedPath = path.dirname(pathToFile);
// console.log(formattedPath);

// ------ sync version (not working with promises) -------

// const files = fs.readdir(formattedPath, (files) => console.log(files));

// fs.readdir(formattedPath, (err, files) => {
//   if (err) {
//     console.error("Error reading directory:", err);
//     return;
//   }
//   files.forEach(function (file) {
//     // Do whatever you want to do with the file
//     console.log(file);
//   });
// });

async function listFiles() {
  try {
    const files = await fs.readdir(formattedPath);
    console.log(files.sort((a, b) => a.localeCompare(b)).join("         "));
  } catch (err) {
    //is it goes to sterror
    console.error("Error reading directory:", err);
  }
}

listFiles();
