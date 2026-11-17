#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the string "cure", as well as the line before that line.
# The output should contain two pairs of two lines of text (with a separator between them).

# -B 1 also prints 1 line Before each match; grep puts -- between separate groups
grep -B 1 cure dialogue.txt
