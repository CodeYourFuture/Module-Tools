import process from "node:process";
import {program} from "commander";
import {promises as fs} from "node:fs";

program
.name("WC clone")
.description("Counting each words in a given file")
.argument("<files...>","one or more files to count the words")
.action(async (files)=>{
    let totalLines = 0;
    let totalWords = 0;
    let totalBytes = 0;
    
    for (const file of files){
        try {
        const content = await fs.readFile(file,"utf-8");
        const size = await fs.readFile(file);

        const lineCount = content.split("\n").length-1;

        const wordCount = content.trim() === "" ? 0 : content.trim().split(/\s+/).length;

        const byteCount = size.length;

        totalLines += lineCount;
        totalWords += wordCount;
        totalBytes += byteCount;

        printCounts({lineCount,wordCount,byteCount,label:file,});
    }

catch (err){
    console.error("No such file or directory");
    process.exit(1);
}
    }

    if (files.length>1)
    {
        printCounts({lineCount:totalLines,
            wordCount:totalWords,
            byteCount:totalBytes,
            label:"Total",
        })
    }

});

function printCounts({lineCount,wordCount,byteCount,label})
{
    let output = "";

    output += lineCount.toString().padStart(7, " ");
    output += wordCount.toString().padStart(7," ");
    output += byteCount.toString().padStart(7," ");

    console.log(`${output} ${label}`);
}

program.parse(process.argv);