#!/usr/bin/python3

import sys
from math import *

def show_sla(n):

    down = 365.25 * 24 * 60 * 60 * ( (100 - n) / 100 )

    h = int(down / (60 * 60))

    m = int(down % 60)

    s = round(down % (60 * 60) % 60 ,1)
    
    time = str(h) + "h " + str(m) + "m " + str(s) + "s"

    return time

if __name__ == "__main__":
    print(show_sla(float(sys.argv[1])))
