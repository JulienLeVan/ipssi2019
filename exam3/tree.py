#!/usr/bin/python3

from math import *
import sys

def show_tree(n):

    # n = int(sys.argv[1])
    # print (type(l))

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

    print("Largeur " + str(largeur))
    print("Tronc " + str(tronc))
    print("Hauteur " + str(hauteur))

    # OK POUR LES BRANCHES, DESSINE LES BRANCHES
    for i in range(largeur):
        print(" "*(largeur-i) + 'X' * ( (2*i+1 - largeur+1)))    

    # test 
    # for i in range(largeur):
    #     print( 'X' * ( (2*i+1 - largeur +1 ) ) )

    # DESSINE LE TRONC
    if tronc == 1:
        for i in range(hauteur):
            print(" " *( (ceil(largeur/2)) ) + "X")
    else:
        for i in range(hauteur):
            print(" "*( (floor(largeur/2)) )  + "XXX")


# print(' '*((ceil(n/2)))+'#')


if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))