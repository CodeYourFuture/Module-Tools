#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player along with the number of times they've played the game.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 3".

hammadhaider@Hammads-MacBook-Pro awk % awk '{print $1, NF-2}' scores-table.txt
Ahmed 3
Basia 3
Mehmet 3
Leila 1
Piotr 5
Chandra 2