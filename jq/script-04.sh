#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output just the names of each player, one per line.
#  output contains 6 lines, each with just one word on it.
#  output does not contain any quote characters.

jq -r '.[].name' scores.json