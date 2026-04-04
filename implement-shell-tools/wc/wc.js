import { promises as fs } from "node:fs";
async function wcJsImplement() {

    let totalLines=0,totalWords=0,TotalBytes=0;
    let words,bytes;
    const commandLineArray=process.argv.slice(2);
    const flags = commandLineArray.filter((item) => item.startsWith("-"));
    
    if(flags.length !==0 )
    {
        commandLineArray.shift();
    }
    
    function printOutput(lines,words,bytes,lable){
      switch (flags[0]) {
        case "-l":
          console.log(`${String(lines).padStart(4)} ${lable}`);
          break;
        case "-w":
          console.log(`${String(words).padStart(4)} ${lable}`);
          break;
        case "-c":
          console.log(`${String(bytes).padStart(4)} ${lable}`);
          break;
        default:
          console.log(
            `${String(lines).padStart(4)}${String(words).padStart(
              4
            )}${String(bytes).padStart(4)} ${lable}`
          );
      }
    }


    for(const file of commandLineArray){
        const buffer = await fs.readFile(file);
        const fileContent=buffer.toString("utf-8");
        bytes=buffer.length;
        TotalBytes += bytes;
        
        const lines=fileContent.split(/\r?\n/);
        let linesCount,wordsCount=0;
        //Calculate count of lines
        if(lines[lines.length-1].trim()===""){
            lines.pop();
            linesCount=lines.length;
            totalLines += linesCount;
        }
        //calculate count of words
        for(const line of lines){
            words=line.trim().split(/\s+/);
            if (words[0].trim() !== ""){
                 wordsCount += words.length;
            }
        }
        totalWords += wordsCount;
        
        printOutput(linesCount,wordsCount,bytes,file);
    }
    
    if(commandLineArray.length>1){
      printOutput(totalLines, totalWords, TotalBytes, "total");
    }
    
}
wcJsImplement();