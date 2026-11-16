#!/bin/bash

set -euo pipefail

# TODO: Write a command to output every line in dialogue.txt said by the Doctor.
# The output should contain 6 lines.

# ^ means "starts with", so this only matches lines where the Doctor is speaking
grep "^Doctor:" dialogue.txt
