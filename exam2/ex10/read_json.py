#!/usr/bin/python3

import json

with open("students.json") as text:
   data = json.load(text)
   print(data)
