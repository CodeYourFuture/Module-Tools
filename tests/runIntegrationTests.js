const { execSync } = require("node:child_process");

function runCommand(command) {
  return execSync(command, { encoding: "utf-8" }).trim();
}

function normalizeOutput(output) {
  return output.replaceAll(/\s+/g, " ").trim();
}

function test(name, systemCommand, nodeCommand) {
  try {
    const expected = normalizeOutput(runCommand(systemCommand));
    const actual = normalizeOutput(runCommand(nodeCommand));
    if (expected === actual) {
      console.log(`✅ ${name} passed`);
    } else {
      console.error(`❌ ${name} failed`);
      console.error(`Expected: "${expected}"`);
      console.error(`Actual:   "${actual}"`);
    }
  } catch (error) {
    console.error(`❌ ${name} failed with error: ${error.message}`);
  }
}

/* CAT TESTS */
test(
  "cat single file",
  "cat implement-shell-tools/cat/sample-files/1.txt",
  "node implement-shell-tools/cat/cat.js implement-shell-tools/cat/sample-files/1.txt",
);

test(
  "cat -n single file",
  "cat -n implement-shell-tools/cat/sample-files/1.txt",
  "node implement-shell-tools/cat/cat.js -n implement-shell-tools/cat/sample-files/1.txt",
);

test(
  "cat multiple files",
  "cat implement-shell-tools/cat/sample-files/*.txt",
  "node implement-shell-tools/cat/cat.js implement-shell-tools/cat/sample-files/*.txt",
);

test(
  "cat -n multiple files",
  "cat -n implement-shell-tools/cat/sample-files/*.txt",
  "node implement-shell-tools/cat/cat.js -n implement-shell-tools/cat/sample-files/*.txt",
);

test(
  "cat -b file",
  "cat -b implement-shell-tools/cat/sample-files/3.txt",
  "node implement-shell-tools/cat/cat.js -b implement-shell-tools/cat/sample-files/3.txt",
);

/* LS TESTS */

test(
  "ls sample-files",
  "ls implement-shell-tools/ls/sample-files",
  "node implement-shell-tools/ls/ls.js implement-shell-tools/ls/sample-files",
);

/* WC TESTS */

test(
  "wc all files",
  "wc implement-shell-tools/wc/sample-files/*",
  "node implement-shell-tools/wc/wc.js implement-shell-tools/wc/sample-files/*",
);

test(
  "wc -l single file",
  "wc -l implement-shell-tools/wc/sample-files/3.txt",
  "node implement-shell-tools/wc/wc.js -l implement-shell-tools/wc/sample-files/3.txt",
);

test(
  "wc -w single file",
  "wc -w implement-shell-tools/wc/sample-files/3.txt",
  "node implement-shell-tools/wc/wc.js -w implement-shell-tools/wc/sample-files/3.txt",
);

test(
  "wc -c single file",
  "wc -c implement-shell-tools/wc/sample-files/3.txt",
  "node implement-shell-tools/wc/wc.js -c implement-shell-tools/wc/sample-files/3.txt",
);

test(
  "wc -l multiple files",
  "wc -l implement-shell-tools/wc/sample-files/*",
  "node implement-shell-tools/wc/wc.js -l implement-shell-tools/wc/sample-files/*",
);
