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

// TASK 2
// Read through this file and predict what it does.
// Leave a comment on any lines if you spot any errors, offering an explanation of the problem.

// Any of the following, not limited to:

// We handle not ok responses, but assume we can use response.body.
// In fetch, if we want to access the body we need to treat it as a stream, not a simple string property.

// The else condition has the same problem, which will not print anything useful

// The way the code is designed, we would only encounter the above error if we first get a not-ok response, so it is difficult to test.

// We are assuming that the response for a correct URL will be a json response, which may not always be the case.