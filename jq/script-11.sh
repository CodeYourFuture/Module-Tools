#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output the total of adding together all scores from all games from all players.
# Output is exactly the number 164.

jq '[.[].scores | add] | add' scores.json