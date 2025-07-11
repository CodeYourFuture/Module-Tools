#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the names of each player, as well as their city.
# Your output should contain 6 lines, each with two words on it, separated by a space.

#Answer
cut -d' ' -f1,2  individual-shell-tools/awk/scores-table.txt

# -f1,2 get the first and second field