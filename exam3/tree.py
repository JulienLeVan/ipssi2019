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

    # BRANCHES
    for i in range(p):
        print(" "*(p-1-i) + 'X' * ( (2*i+1)))    
        
    # TRONC
    if tronc == 1:
        for i in range(hauteur):
            print(" " *( (ceil(largeur/2))-1 ) + "X")
    else:
        for i in range(hauteur):
            print(" "*( (floor(largeur/2))-1 )  + "XXX")


if __name__ == "__main__":
    out = (show_tree(int(sys.argv[1])))
    print(out)