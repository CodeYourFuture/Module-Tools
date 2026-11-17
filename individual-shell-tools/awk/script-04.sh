#!/bin/bash

set -euo pipefail

# TODO: Write a command to output just the names of each player in London along with the score from their last attempt.
# Your output should contain 3 lines, each with one word and one number on it.
# The first line should be "Ahmed 4".

# the pattern $2 == "London" only runs the action on London lines; $NF is the last field (NF = number of fields), i.e. the last attempt's score
awk '$2 == "London" {print $1, $NF}' scores-table.txt
