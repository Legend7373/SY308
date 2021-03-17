# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW4 problem 5
Usage: 
'''
# Imported libraries
from sys import argv
import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def writeKeys(bin_file):
    key_file = open(bin_file, 'wb')
    new_key = get_random_bytes(16)
    key_file.write(new_key)
    key_file.close()
    

if __name__ == "__main__":
    if len(argv) < 2:
        exit()
    writeKeys((argv[1]))