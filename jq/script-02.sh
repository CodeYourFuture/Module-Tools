#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# Command to output the address of the person, all on one line, with a comma between each line.
# Output is the string "35 Fashion Street, London, E1 6PX", but does not contain any quote characters.

# Solution 1 
# jq -rj '.address.[0] + ", ",.address.[1] + ", ",.address.[2] + "\n"' person.json 

# Solution 2
jq -rj '.address | join(", ") + "\n"' person.json 