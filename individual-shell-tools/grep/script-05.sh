#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the string "cure", as well as the line before that line.
# The output should contain two pairs of two lines of text (with a separator between them).
path="/Users/cyf/Documents/SDC/Module-Tools/individual-shell-tools/grep/dialogue.txt"
grep -B 1 'cure' "$path"