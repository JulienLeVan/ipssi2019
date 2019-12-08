#!/usr/bin/python3

import sys
import os

#C:\Users\Julien\Desktop\DEVOPS
# /mnt/c/Users/Julien/Desktop/DEVOPS

dos = sys.argv[1]


print(dos)

print(os.listdir( dos ))
print(os.path.getsize(dos))