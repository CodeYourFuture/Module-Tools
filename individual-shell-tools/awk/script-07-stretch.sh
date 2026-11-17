#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output just the names of each player along with the total of adding all of that player's scores.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 15". The second line should be "Basia 37"

# for each line: reset total to 0, loop over fields 3 to NF (all the scores) adding each $i, then print the name and its total
awk '{total = 0; for (i = 3; i <= NF; i++) total += $i; print $1, total}' scores-table.txt
