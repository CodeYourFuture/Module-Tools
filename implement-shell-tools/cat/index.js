import process from "node:process";
import { promises as fs } from "node:fs";


//one for 1 and 3
async function printOneOrMore(listOfFiles) {
    for (const file of listOfFiles) {
        const content = await fs.readFile(file, "utf-8");
        console.log(content);
    }
}
    

// // 2 * `cat -n sample-files/1.txt`
// async function caseTwo(oneFile) {
//     const content = await fs.readFile(oneFile, "utf-8");
//     const separatedToLines = content.split('\n')
//     separatedToLines.forEach((line, index) => {
//         console.log(`${index + 1} ${line}`)
//     })
// }

// // 4 * `cat -n sample-files/*.txt`
// async function caseFour(listOfFiles) {
//     for (const file of listOfFiles) {
//         const content = await fs.readFile(one, "utf-8");

//         const separatedToLines = content.split('\n')
//         separatedToLines.forEach((line, index) => {
//         console.log(`${index + 1} ${line}`)
//     })
// }
    
// }

//one instead
//  2 * `cat -n sample-files/1.txt`
// 4 * `cat -n sample-files/*.txt`

async function caseTwoAndFour(listOfFiles) {
    for (const file of listOfFiles) {
        const content = await fs.readFile(file, "utf-8");

        const separatedToLines = content.split('\n')
        separatedToLines.forEach((line, index) => {
            console.log(`${index + 1} ${line}`)
    })
}
    
}

// `cat -b sample-files/3.txt`
async function caseFive(listOfFiles) {
    for (const file of listOfFiles) {
        const content = await fs.readFile(file, "utf-8");
        const separatedToLines = content.split('\n');

        let countingOnlyFullLines = 1
        separatedToLines.forEach((line, index) => {
            if (line !== '') {
                console.log(`${countingOnlyFullLines} ${line}`)
                countingOnlyFullLines++
            } else {
                console.log('')
            }
            
        })
    }

}


const argv = process.argv.slice(2);

switch (argv[0]) {
    case '-n':
        await caseTwoAndFour(argv.slice(1));
        break;

    case '-b':
        await caseFive(argv.slice(1));
        break;

    default:
        await printOneOrMore(argv);
        break;
}