import process from "node:process";
import { promises as fs } from "node:fs";

const arrArgv = process.argv.slice(2);

const lines = arrArgv.includes("-l");
const words = arrArgv.includes("-w");
const bytes = arrArgv.includes("-c");

const noFlags = !lines && !words && !bytes;

const paths = arrArgv.filter((argv) => !argv.startsWith("-"));

for (let path of paths) {
  const context = await fs.readFile(path, "utf-8");

  const countLines = context.split(/\r?\n/).length;
  const countWords = context.split(/\s+/).length;
  const countBytes = Buffer.byteLength(context, "utf-8");

  let startInput = "";

  if (noFlags || lines) {
    startInput += `${countLines} `;
  }

  if (noFlags || words) {
    startInput += `${countWords} `;
  }

  if (noFlags || bytes) {
    startInput += `${countBytes} `;
  }

  startInput += path;

  console.log(startInput);
}
