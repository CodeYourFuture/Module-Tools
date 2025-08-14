#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# TODO: Write a command to output the name of the person.
# Your output should be exactly the string "Selma", but should not contain any quote characters.
path="/Users/cyf/Documents/SDC/Module-Tools/jq/person.json"
jq -r '.name' $path