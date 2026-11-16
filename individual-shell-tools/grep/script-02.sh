#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt that contains the word Doctor (regardless of case).
# The output should contain 9 lines.

# -i ignores case, so it matches Doctor, doctor, DOCTOR, etc.
grep -i Doctor dialogue.txt
