#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the name of every `.txt` file in this directory which contains a line of dialogue said by the Doctor.
# The output should contain two filenames.
grep -l "Doctor:" "$(dirname "$0")"/*.txt | while IFS= read -r filepath; do
    basename "$filepath"
done