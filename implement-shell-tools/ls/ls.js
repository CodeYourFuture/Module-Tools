import { promises as fs } from "node:fs";
async function listDir() {
    const flag = process.argv[2];
    const fileNamePattern = process.argv[3] || process.cwd();
    console.log(fileNamePattern);
    console.log(flag);
   const fileListArray = await fs.readdir(fileNamePattern);
   console.log(fileListArray);
  
   
   for(const item of fileListArray){
    console.log(item);
   }
  
}
listDir();