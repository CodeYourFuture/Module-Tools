#!/bin/bash

user_command=(${USER_COMMAND:-"node cat.js"})

function test() {
  args=${@}
  echo "======"
  echo "Testing cat ${args}"
  echo "======="
  diff -y <(cat ${args[@]}) <(${user_command[@]} ${args[@]})
  echo ""
  echo ""
}

test 'sample-files/1.txt'
test '-n' 'sample-files/1.txt'
test 'sample-files/*.txt'
test '-n' 'sample-files/*.txt'
test '-b' 'sample-files/3.txt'
