#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in London along with the score from their last attempt.
# Your output should contain 3 lines, each with one word and one number on it.
# The first line should be "Ahmed 4".

#Answer
awk '$2 == "London" {print $1, $NF}' individual-shell-tools/awk/scores-table.txt

#$NF is the number of fields which give me the last field in the line.