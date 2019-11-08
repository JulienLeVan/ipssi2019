#!/usr/bin/python3


file = open("docker-compose.yml", "r")
##lines = file.readlines()
##file.close

for line in file:
   print(line)

file.close
