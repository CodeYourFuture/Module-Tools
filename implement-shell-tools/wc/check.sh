#!/bin/bash

user_command=(${USER_COMMAND:-"node wc.js"})

function test() {
  args=${@}
  echo "======"
  echo "Testing wc ${args}"
  echo "======="
  diff -y <(wc ${args[@]}) <(${user_command[@]} ${args[@]})
  echo ""
  echo ""
}

test 'sample-files/*'
test '-l' 'sample-files/3.txt'
test '-w' 'sample-files/3.txt'
test '-c' 'sample-files/3.txt'
test '-l' 'sample-files/*'
