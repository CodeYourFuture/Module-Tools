#!/bin/bash

set -euo pipefail

# TODO: Write a command to output input.txt replacing every occurrence of the string "We'll" with "We will".
# The output should contain 11 lines.

# as here we got only one occurance:
sed "s/We'll/We will/" input.txt
# But if there was more occurance, the code would be:
sed "s/We'll/We will/g" input.txt