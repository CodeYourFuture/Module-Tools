#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the word Doctor (regardless of case).
# The output should contain 9 lines.
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/grep/dialogue.txt"
grep -i 'Doctor' "$path"