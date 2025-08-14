#!/bin/bash

set -euo pipefail

# The input for this script is the scores-table.txt file.
# TODO: Write a command to output scores-table.txt, with lines sorted by the person's name.
# The first line of your output should be "Ahmed London 1 10 4" (with no quotes). And the third line should be "Chandra Birmingham 12 6".
sort scores-table.txt

Ahmed London 1 10 4
Basia London 22 9 6
Chandra Birmingham 12 6
Leila London 1
Mehmet Birmingham 3 12 17
Piotr Glasgow 15 2 25 11 8
