#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# TODO: Write a command to output the total of adding together all players' first scores.
jq 'map(.scores[0]) | add' scores.json

# Your output should be exactly the number 54.
