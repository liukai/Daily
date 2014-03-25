#!/bin/bash

USAGE="USAGE:\n"
USAGE+="    append.sh <file> [<appended line>]"

if [[ $# < 1 ]]; then
  echo "append.sh requires at least parameters: \n" $USAGE
  exit 1
fi

FILE=$1
if [[ $# = 1 ]]; then
  cat >> $FILE 
else
  shift
  echo $* >> $FILE
fi
