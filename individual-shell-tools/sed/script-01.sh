#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt with all occurrences of the letter `i` replaced with `I`.
# The output should contain 11 lines.
# The first line of the output should be: "ThIs Is a sample fIle for experImentIng with sed.".

sed s/i/I/g ./input.txt

#   **** FYI: In the line 7,it seems there is a mistake, as example for output looks like `with` is not replaced with `wIth`, but it should be replaced. ****