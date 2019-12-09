#!/usr/bin/python3

import sys
from datetime import *
import calendar
from tree import show_tree

def show_noel(n):

    if len(n) > 1:
        day = n[1]
    else:
        day = datetime.now().strftime('%Y-%m-%d')

    d = day.split("-")    
    
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])

    if year<=2019:
        d1 = date(year, 12, 25) - date(year, month, day)
    else:
        d1 = date(year, 12, 25) - date(year, month, day)

    t = str(d1.days) + " days before christmas\n"

    d = str(day)
    
    if  day==25 and month==12 and year==2019 :
    
        return show_tree(10)
    
    else:
       
        t = t + calendar.month(year,month).replace( d, "("+d+")", 1)
           
        while month <= 10:
            t = t + calendar.month(year,(month+1))
            month = month + 1
            
        t = t + calendar.month(year,12).replace( "25", "[25]", 1)
        
        return t


if __name__ == "__main__":
    print(show_noel(sys.argv))