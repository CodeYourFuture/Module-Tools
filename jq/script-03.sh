#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# TODO: Write a command to output the name of the person, then a comma, then their profession.
# Your output should be exactly the string "Selma, Software Engineer", but should not contain any quote characters.

# Join works on arrays thats why we need to to put values of name and profession in a array to be able to use join
jq -r '[.name, .profession] | join(", ")' person.json 
