#!/bin/bash

set -euo pipefail

# TODO: Write a command to output the name of every `.txt` file in this directory which contains a line of dialogue said by the Doctor.
# The output should contain two filenames.

grep Doctor -il *.txt

dialogue.txt
dialogue-2.txt
dialogue-3.txt
