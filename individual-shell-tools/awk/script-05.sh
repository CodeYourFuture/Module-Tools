#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player along with the number of times they've played the game.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 3".

# NF is the number of fields on the line; subtracting 2 (name and city) leaves the number of scores, i.e. games played
awk '{print $1, NF - 2}' scores-table.txt
