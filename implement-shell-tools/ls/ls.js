import { promises as fs } from "node:fs";
async function listDir() {
   let finalFileList;
   const flag = process.argv[2];
   const argvArray=process.argv.slice(2);
   
   const flags=argvArray.filter(item => item.startsWith('-'));
  
   const Path =
   argvArray.filter((item) => !item.startsWith("-")) || process.cwd();
    
   const fileListArray = await fs.readdir(Path[0] || process.cwd());
   if (flags.includes('-a')){
    finalFileList=fileListArray;
   }else{
   finalFileList=fileListArray.filter(file => !file.startsWith('.'));
   }
   
  
   
   for(const item of finalFileList){
    console.log(item);
   }
  
}
listDir();