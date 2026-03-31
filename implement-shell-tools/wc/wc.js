import { program } from "commander";
import { promises as fs } from "node:fs";

//configuring 
program
  .name("wc")
  .description("Print newline, word, and byte counts for each file")
  .option("-l, --lines", "Print the newline counts")
  .option("-w, --words", "Print the word counts")
  .option("-c, --bytes", "Print the byte counts")
  .argument("<files...>", "File paths to process")
//Interpret the program
  program.parse()
const options = program.opts()
const files = program.args //Interpreting parsed data


//helper function to calculate all counts 
async function getCounts(file){
  const content = await fs.readFile(file, "utf-8");
  const lineCount = content.split("\n").length -1;//split("\n") returns one more element than the actual number so length-1,
  const wordCount = content.trim().split(/\s+/).length;
  const byteCount = Buffer.byteLength(content, "utf-8"); //Calculate how many bytes the string uses in UTF-8 (important because some characters use more than 1 byte)
  return { lineCount, wordCount, byteCount };
}
//helper to remove duplicated output logic 
function formatOutput(lines, words, bytes, filename, options) {
   let formattedOutput = ""; 
   if (options.lines) formattedOutput += `${lines} `; 
   if (options.words) formattedOutput+= `${words} `; 
   if (options.bytes) formattedOutput += `${bytes} `; 
   if (!options.lines && !options.words && !options.bytes) { // default: print all three 
     formattedOutput += `${lines} ${words} ${bytes} `; 
    }
    return formattedOutput + filename; 
  }
 //Initiating totals
let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;

for (const file of files) {
  const { lineCount, wordCount, byteCount } = await getCounts(file);

  totalLines += lineCount;
  totalWords += wordCount;
  totalBytes += byteCount;

  const formatted = formatOutput(lineCount, wordCount, byteCount, file, options);
  console.log(formatted);
}
//Print totals if multiple files
if (files.length > 1) {
  const formattedTotals = formatOutput(totalLines, totalWords, totalBytes, "total", options);
  console.log(formattedTotals);
}




  