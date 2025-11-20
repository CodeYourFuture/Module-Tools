import { promises as fs } from "node:fs";
async function wcJsImplement() {
    let totalLines=0,totalWords=0,TotalBytes=0;
    let words;
    const commandLineArray=process.argv.slice(2);
    console.log(commandLineArray);
    for(const file of commandLineArray){
        const fileContent=await fs.readFile(file , 'utf-8');
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
        totalWords = +wordsCount;

        console.log(file);
        console.log(fileContent)
        console.log(lines);
        console.log(linesCount);
        console.log(totalLines);
         console.log(words);
         console.log(wordsCount);
        console.log(totalWords);
    }
}
wcJsImplement();