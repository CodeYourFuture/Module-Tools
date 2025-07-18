#!/bin/bash
#!/bin/bash

set -euo pipefail

sort -k3n scores-table.txt | tail -n2 | head -n1

# The input for this script is the scores-table.txt file.
# TODO: Write a command to output scores-table.txt, with shows the line for the player whose first score was the second highest.
# Your output should be: "Piotr Glasgow 15 2 25 11 8" (without quotes).
