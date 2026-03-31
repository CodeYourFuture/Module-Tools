import { program } from "commander";
import { error } from "node:console";
import { promises as fs, link } from "node:fs";

program
  .name("wc")
  .description("wc implementation")
  .argument("<paths...>", "the file path to process");
program.parse();

const paths = program.args;
const total = {
  linesCounter: 0,
  wordsCounter: 0,
  characterCounter: 0,
};
try{
for (const path of paths) {
  const content = await fs.readFile(path, "utf-8");

  const linesCounter = content.split("\n").length - 1;
  const wordsCounter = content.trim().split(/\s+/).length;
  const characterCounter = content.length;

  total.linesCounter += linesCounter;
  total.wordsCounter += wordsCounter;
  total.characterCounter += characterCounter;

  console.log(` ${linesCounter}  ${wordsCounter} ${characterCounter} ${path}`);
}
if (paths.length > 1)
  console.log(
    ` ${total.linesCounter}  ${total.wordsCounter} ${total.characterCounter} total`,
  );
}catch(error){
    console.log(error.message);
}