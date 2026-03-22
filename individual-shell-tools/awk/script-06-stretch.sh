#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.
awk '{total += $3} END {print total}' scores-table.txt
# TODO: Write a command to output the total of adding together all players' first scores.
# Your output should be exactly the number 54.
