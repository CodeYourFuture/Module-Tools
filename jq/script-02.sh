#!/bin/bash

set -euo pipefail

# The input for this script is the person.json file.
# TODO: Write a command to output the address of the person, all on one line, with a comma between each line.
# Your output should be exactly the string "35 Fashion Street, London, E1 6PX", but should not contain any quote characters.

#note to self:
# What Each Part Does
# jq → Calls the jq tool.
# -r → Removes quotes from the output (so the result is a plain string, not JSON).
# .address → Extracts the address array from the JSON.
# | join(", ") →
# Takes all elements in the array: ["35 Fashion Street", "London", "E1 6PX"]
# Joins them into a single string, separated by ", ".
# ❌ Do NOT use .address[] if address is an array of strings
# ✅ Use .address[] when address is an array of objects

jq -r '.address | join(", ")' person.json
