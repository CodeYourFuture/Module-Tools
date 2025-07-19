#!/bin/bash

set -euo pipefail

# The input for this script is the scores-table.txt file.
# TODO: Write a command to output scores-table.txt, with shows the line for the player whose first score was the second highest.
# Your output should be: "Piotr Glasgow 15 2 25 11 8" (without quotes).

sort -rnk3 scores-table.txt | sed -n '2p'

#sed -n '2p' is print the second line of the sorted output
