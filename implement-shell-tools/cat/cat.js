import { promises as fs } from "node:fs";
import { glob } from "glob";
async function readFile() {
  let fileNamePattern;
  let flag;
  if (process.argv[2].startsWith("-")) {
    flag = process.argv[2];
    fileNamePattern = process.argv[3];
  } else {
    fileNamePattern = process.argv[2];
  }

  const filesNameArray = await glob(fileNamePattern);
  filesNameArray.sort();
  let lineNumber = 1;

  for (const file of filesNameArray) {
    const fileContent = await fs.readFile(file, "utf-8");
    if (flag == null) {
      console.log(fileContent);
    } else {
      const linesOfText = fileContent.split(/\r?\n/);
      if (linesOfText[linesOfText.length - 1].trim() === "") {
        linesOfText.pop();
      }

      for (const line of linesOfText) {
        if (line.trim() === "" && flag === "-b") {
          console.log(line);
        } else {
          console.log(`${lineNumber} ${line}`);
          lineNumber++;
        }
      }
    }
  }
}

readFile();
