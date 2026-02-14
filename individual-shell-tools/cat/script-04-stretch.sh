#!/bin/bash

set -euo pipefail

# NOTE: This is a stretch exercise - it is optional.

# TODO: Write a command to output the contents of all of the files in the helper-files directory to the terminal.
# We also want to see the line numbers in the output, but we want line numbers not to reset at the start of each file.
#
# The output of this command should be something like:
# 1 Once upon a time...
# 2 There was a house made of gingerbread.
# 3 It looked delicious.
# 4 I was tempted to take a bite of it.
# 5 But this seemed like a bad idea...
cat -n ../helper-files/*.txt

#On macOS, this does not produce the expected result. Each file's line numbering resets instead of continuing. To get the expected behavior, we can use the awk command:
# awk '{print NR, $0}' ../helper-files/helper-1.txt ../helper-files/helper-2.txt ../helper-files/helper-3.txt
# However, I did not add that solution as we are in a cat exercise.