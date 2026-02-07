#!/bin/bash

set -euo pipefail

# The input for this script is the scores-table.txt file.
# TODO: Write a command to output scores-table.txt, with shows the line for the player whose first score was the second highest.
# Your output should be: "Piotr Glasgow 15 2 25 11 8" (without quotes).
path="/Users/cyf/Documents/SDC/Module-Tools/shell-pipelines/sort-uniq-head-tail/scores-table.txt"
sort -t ' ' -k3 -n -r $path | awk 'NR==2'