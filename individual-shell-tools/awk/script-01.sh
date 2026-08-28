#!/bin/bash

set -euo pipefail

awk '{print $1}' scores-table.txt
