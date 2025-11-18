import { promises as fs } from "node:fs";
import { glob } from "glob";
 async function readFile(){
    const fileNamePattern=process.argv[2];
    const filesNameArray=await glob(fileNamePattern);
    filesNameArray.sort();
    for(const file of filesNameArray){
        const fileContent=await fs.readFile(file,"utf-8");
        console.log(fileContent);
    }

    
 }
 readFile();