#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output the total of adding together all players' first scores.
# Your output should be exactly the number 54.

# total += $3 adds each player's first score as awk reads each line; the END block runs once after the last line and prints the sum
awk '{total += $3} END {print total}' scores-table.txt
