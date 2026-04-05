#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the word Doctor (regardless of case).
grep -i "doctor" dialogue.txt
# The output should contain 9 lines.
