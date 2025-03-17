#!/bin/bash

set -euo pipefail

# The input for this script is the scores.json file.
# Command to output the total of adding together all players' first scores.
# output is exactly the number 54.

jq '[.[].scores[0]] | add' scores.json
