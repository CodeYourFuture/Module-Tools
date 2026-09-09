import process from "node:process";
import readline from "node:readline";

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

rl.question("What URL should we fetch?\n> ", async (url) => {
	const response = await fetch(url);
	if (!response.ok) {
		if (response.body.toLowerCase().includes("permission")) {
			console.error("You didn't have permission to get that URL");
		} else {
			console.error(`The request failed - body: ${response.body}`);
		}
		process.exit(1);
	}

	const contents = await response.json();

	console.log(contents);

	rl.close();
});

// Task: Leave a comment on any line that you can see has some errors explaining what you think the problem is
