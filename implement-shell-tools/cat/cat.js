import {program} from "commander";
import {promises as fs} from "node:fs";
import process from "node:process";

program 
.name ("cat")
.description ("A JS clone for unix command cat")
.argument("<files...>","One or more files to reach and print")
.option("-n", "number all output lines")
.action(async (files,options)=> {
  for (const filePath of files){
    try {
        const content = await fs.readFile(filePath,"utf8");
        if (options.n)
        {
            const lines = content.trimEnd().split("\n");
            lines.forEach((line,index) => {
            console.log(`${index+1} \t ${line}`);
            });
        }
        else 
        {
            process.stdout.write(content);
        }


    }
    catch(error)
    {
        console.error("No such file or directory");
        process.exit(1);
    }

  }  

});

program.parse(process.argv);