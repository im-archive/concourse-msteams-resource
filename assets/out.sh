#!/usr/bin/env bash
set -e

exec 3>&1 # make stdout available as fd 3 for the result
exec 1>&2 # redirect all output to stderr for logging

# echo "*** Number of args:"
# echo $#
# echo "*** Arg 1:"
# echo $1
# echo "*** Arg 2:"
# echo $2
# echo "*** Arg 3:"
# echo $3

$(dirname $0)/lib/out.py $1 $2

printf '{"version":{}}' >&3