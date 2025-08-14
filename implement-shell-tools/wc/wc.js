const { promises: fs } = require("fs");

async function wc(filePath) {
  try {
    const data = await fs.readFile(filePath, "utf8");
    const lines = data.split("\n").length;
    const words = data.split(/\s+/).filter(Boolean).length;
    const bytes = Buffer.byteLength(data, "utf8");

    console.log(`${lines} ${words} ${bytes} ${filePath}`);
  } catch (err) {
    console.error(`no access '${filePath}': No such file or folder`);
  }
}

const filePath = process.argv[2];
if (!filePath) {
  console.error(" <file> doesn't exist");
  process.exit(1);
}

wc(filePath);
