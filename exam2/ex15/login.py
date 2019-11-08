#!/usr/bin/python3

import hashlib

y = hashlib.md5("ipssi".encode()).hexdigest()

print('md5 "ipssi" : ', y)

def compare_pass(test):

    x = hashlib.md5(test.encode()).hexdigest()

    print('md5    pass : ', x)

    if x == y :
        print('login ok')
    else:
        print('login failed')
