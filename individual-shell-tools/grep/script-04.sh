#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that does not contain the word "Hello" (regardless of case).
# The output should contain 10 lines.
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/grep/dialogue.txt"
grep -vi 'Hello' "$path"