# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW1 Problem 5
Usage: python3 program 'ciphertext'
'''
# Imported libraries
from sys import argv 
# Globals

def main():
    '''
    Description: Takes ciphertext from command line argument. Shifts each char in the ciphertext
                 for k=0 ... k=25, then finds the letter that corresponds to and and prints out the 
                 decrypted string for each k. 
    '''
    try:
        ciphertext = argv[1]
    except:
        print("Usage: python3 program 'ciphertext'")
        exit()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_alpha = list(letters)
    for shift in range(0,26):
        plain_txt = ""
        for char in ciphertext:
            cur_index = list_alpha.index(char)
            decrypt_index = (cur_index - shift) % 26
            decrypt_char = list_alpha[decrypt_index]
            plain_txt += decrypt_char
        print("k= " + str(shift) + " : " + plain_txt)
    return
if __name__ == '__main__':
    main()