#!/usr/bin/python3

file = open("docker-compose.yml", "r")

word = "image:"

for line in file:
    if word in line:
        print(line.strip().split()[1])


file.close
