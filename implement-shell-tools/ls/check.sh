#!/bin/bash

user_command=(${USER_COMMAND:-"node ls.js"})

function test() {
  args=${@}
  echo "======"
  echo "Testing ls ${args}"
  echo "======="
  diff -y <(/bin/ls ${args[@]}) <(${user_command[@]} ${args[@]})
  echo ""
  echo ""
}

test
test '-1'
test '-1' 'sample-files'
test '-1' '-a' 'sample-files'
