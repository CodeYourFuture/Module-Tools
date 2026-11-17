#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the name of every `.txt` file in this directory which contains a line of dialogue said by the Doctor.
# The output should contain two filenames.

# -l prints only the names of files that contain a match, not the lines themselves
grep -l "^Doctor:" *.txt
