import { promises as fs } from "node:fs";
async function listDir() {
   const flag = process.argv[2];
   const fileNamePattern = process.argv[3] || process.cwd();
    //console.log(fileNamePattern);
    //console.log(flag);
   const fileListArray = await fs.readdir(fileNamePattern);
   const visibleFileListArray=fileListArray.filter(file => !file.startsWith('.'));
   //console.log(fileListArray);
   //console.log(visibleFileListArray);
   
   for(const item of visibleFileListArray){
    console.log(item);
   }
  
}
listDir();