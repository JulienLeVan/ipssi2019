#!/usr/bin/python3

from math import *
import sys

def show_tree(n):

    # LARGEUR DU SAPIN
    if n%2 == 0 :
        largeur = n + 1
    else:
        largeur = n

    # TAILLE DU TRONC
    if n <= 3:
        tronc = 1
    else :
        tronc = 3

    # HAUTEUR DU  TRONC
    hauteur = floor(n/5) + 1

    p = int(largeur/2)+1

    t = ""

    # BRANCHES
    for i in range(p):
        t = t + (" " * (p-1-i) + 'X' * ((2*i+1)) )
        t = t + "\n"

    # TRONC
    for i in range(hauteur):
        if tronc == 1:
            t = t + (" " * ( (ceil(largeur/2)) -1 ) + "X")
            t = t 
        else:
            t = t + (" " * ( (floor(largeur/2) ) -1 )  + "X" * 3)
            t = t + "\n"
            
    t = t[:-1]   
    
    return t

if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))
