import { promises as fs } from "node:fs";
async function listDir() {
   const fileListArray = await fs.readdir("./");
   //console.log(fileListArray);
   const flag = process.argv[2];
   const fileNamePattern = process.argv[3];
   for(const item of fileListArray){
    console.log(item);
   }
  
}
listDir();