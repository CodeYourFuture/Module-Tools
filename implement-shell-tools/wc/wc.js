import { program } from "commander";
import { promises as fs } from "node:fs";
import path from "node:path";
import { stat } from "node:fs/promises";

program
  .name("my-wc")
  .description("simplified implementation of wc")
  .argument("[paths...]", "One or more file or directory paths")
  .option("-l, --line", "count lines")
  .option("-w, --word", "count words")
  .option("-c, --character", "count characters");

program.parse();

const filePaths = program.args.length > 0 ? program.args : ['.'];
const options = program.opts();

const countContent = (content) => {
    const lines = content.split('\n').length;
    const words = content.trim().split(/\s+/).filter(Boolean).length;
    const characters = content.length;
    return { lines, words, characters };
};

const total = {
    lines: 0,
    words: 0,
    characters: 0
};

(async () => {
    let fileCount = 0;

    for (const inputPath of filePaths) {
        try {
            const stats = await stat(inputPath);
            if (stats.isDirectory()) {
                console.log(`${inputPath} is a directory. Skipping.`);
                continue;
            }

            const content = await fs.readFile(inputPath, "utf-8");
            const { lines, words, characters } = countContent(content);

            total.lines += lines;
            total.words += words;
            total.characters += characters;
            fileCount++;

            let output = "";
            if (options.line) output += `${lines.toString().padStart(8)} `;
            if (options.word) output += `${words.toString().padStart(8)} `;
            if (options.character) output += `${characters.toString().padStart(8)} `;

            // If no options given, show all
            if (!options.line && !options.word && !options.character) {
                output += `${lines.toString().padStart(8)} `;
                output += `${words.toString().padStart(8)} `;
                output += `${characters.toString().padStart(8)} `;
            }

            output += inputPath;
            console.log(output);
        } catch (err) {
            console.error(`Error reading "${inputPath}": ${err.message}`);
        }
    }

    // Print total only if multiple files were processed
    if (fileCount > 1) {
        let output = "";
        if (options.line) output += `${total.lines.toString().padStart(8)} `;
        if (options.word) output += `${total.words.toString().padStart(8)} `;
        if (options.character) output += `${total.characters.toString().padStart(8)} `;

        if (!options.line && !options.word && !options.character) {
            output += `${total.lines.toString().padStart(8)} `;
            output += `${total.words.toString().padStart(8)} `;
            output += `${total.characters.toString().padStart(8)} `;
        }

        output += "total";
        console.log(output);
    }
})();
