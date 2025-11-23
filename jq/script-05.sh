#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output the names of each player, as well as their city.
#  output contains 6 lines, each with two words on it.

jq -r '.[] | .name + " " + .city' scores.json