#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt said by the Doctor.
# The output should contain 6 lines.

grep "^Doctor" dialogue.txt

# ^ - ensures "Doctor" word appears at the start of the line.

