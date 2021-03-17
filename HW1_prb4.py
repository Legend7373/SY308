# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW1 Problem 4
Usage: 
'''
# Imported libraries
from sys import argv
import random 
# Globals

def main():
    '''
    Description: Problem 2
    '''
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    array = []
    l1 = ""
    l2 = []
    l3 = []
    cipher = "NZRAGNFGSYFPLQCNABHAFNGZUAANSVHUBHXVXWANANFAGSLUULVMLBEWRJLUYHYUAANWKNZVXVRHXEIENHWNPWFXJBJHRL"
    print(len(cipher))
    for i in cipher:
        array.append(i)

    for char in LETTERS:
        answer = (array.count(char))
        print(char +" : "+ str(answer)) 
    ciphertext_int = [ord(i) for i in cipher]
    print(ciphertext_int)
    i =2
    while i <= 94:
        l1 += (cipher[i])
        i+=3
    print(l1)

    #print(decrypt(cipher, "E"))
    return

    
   
if __name__ == '__main__':
    main()