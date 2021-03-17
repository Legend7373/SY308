# !/usr/bin/env python3 
'''
Name: MIDN Austin D Andres  m220156
Section:  SY308 - 4001
Description: HW3 problem 4
Usage: 
'''
# Imported libraries
from sys import argv
import sys
from os import urandom 


def generateBitStream(n):    
    random_bytes = bytearray(urandom(n))
    bytes_str = ""
    byte_bin = (random_bytes)
   # print(byte_bin)
    return byte_bin

def writeKeys(key_len, bin_file):
    key_file = open(bin_file, 'wb')
    new_key = ""
    new_key = generateBitStream(key_len)
    key_file.write(new_key)
    key_file.close()
    

if __name__ == "__main__":
    if len(argv) < 3:
        exit()
    writeKeys(int(argv[1]), argv[2])

    
 