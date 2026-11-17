#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that does not contain the word "Hello" (regardless of case).
# The output should contain 10 lines.

# -i ignores case and -v inverts the match, so only lines WITHOUT "hello" are printed
grep -iv hello dialogue.txt
