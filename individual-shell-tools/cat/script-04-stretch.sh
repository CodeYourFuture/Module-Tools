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

# i didn't get this phrase "we want line numbers not to reset at the start of each file."
# so there are two ways to do it
cat -n ../helper-files/*txt # -n number the blank lines and filled out lines
cat ../helper-files/*.txt |nl # skips the blank lines and comes only filled out lines
