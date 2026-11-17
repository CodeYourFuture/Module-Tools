#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the number of lines in dialogue.txt that contain the word Doctor (regardless of case).
# The output should be exactly the number 9.

# -i ignores case and -c counts the matching lines instead of printing them
grep -ic doctor dialogue.txt
