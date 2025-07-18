#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# TODO: Write a command to output the name of the person.
# Your output should be exactly the string "Selma", but should not contain any quote characters.

#ANSWER
jq -r '.name' person.json
#-r to remove the default '' jq adds tgo strings ,jq '.name' extracts the value of the name filed.
