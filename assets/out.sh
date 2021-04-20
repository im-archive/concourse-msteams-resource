#!/usr/bin/env bash
set -e

exec 3>&1 # make stdout available as fd 3 for the result
exec 1>&2 # redirect all output to stderr for logging

$(dirname $0)/lib/out.py $1 <&0

printf '{"version":{}}' >&3