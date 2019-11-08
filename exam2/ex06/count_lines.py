#!/usr/bin/python3

import sys

#text = sys.argv

file = open(sys.argv[1], "r")

i = 0

for line in file:
    i = i+1

print(str(i))
