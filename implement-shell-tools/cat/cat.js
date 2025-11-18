import { promises as fs } from "node:fs";
 async function readFile(){
    const fileName=process.argv[2];
    const fileContent=await fs.readFile(fileName , 'utf-8');
    console.log(fileContent);
 }
 readFile();