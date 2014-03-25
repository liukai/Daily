#!/usr/bin/python
import sys

USAGE="""%s <begin> <end> <file>
  - If begin > end, lines will be printed reversely.""" % sys.argv[0]

def report_error_and_exit(msg):
    print >> sys.stderr, "Too few parameters!"
    print USAGE
    sys.exit(1)

if len(sys.argv) < 4:
    report_error_and_exit("Too few parameters")

try:
    begin, end = int(sys.argv[1]), int(sys.argv[2])
except ValueError:
    report_error_and_exit("Invalid range!")

if begin == end:
    report_error_and_exit("begin == end.")

print "".join(list(open(sys.argv[3]))[begin : end])
