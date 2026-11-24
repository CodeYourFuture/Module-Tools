#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# TODO: Write a command to output the name of the person, then a comma, then their profession.
# Your output should be exactly the string "Selma, Software Engineer", but should not contain any quote characters.

# Put the name and job in a list, then join them with a comma and a space.
jq -r '[.name, .profession] | join(", ")' person.json
