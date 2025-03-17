#!/bin/bash

set -euo pipefail

# The input for this script is the scores-table.txt file.
# Command to output scores-table.txt, with shows the line for the player whose first score was the second highest.
# Your output should be: "Piotr Glasgow 15 2 25 11 8" (without quotes).

sort  -nr -k3 scores-table.txt | head -2 | tail -1