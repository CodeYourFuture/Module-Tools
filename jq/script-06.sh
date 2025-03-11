#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# TODO: Write a command to output just the names of each player along with the score from their first attempt.
# Your output should contain 6 lines, each with one word and one number on it.
# The first line should be "Ahmed 1" with no quotes.
jq -r '.[] | "\(.nam
e) \(.scores[0])" ' scores.json
Ahmed 1
Basia 22
Mehmet 3
Leila 1
Piotr 15
Chandra 12