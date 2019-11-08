#!/usr/bin/python3

import datetime

def logthis(a):
   fichier = open("python.log", "a")
   date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   text = date + " " + str(a)
   fichier.write(text+"\n")
   fichier.close


