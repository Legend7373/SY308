
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
#GLOBALS
def Decrypt(key_file, cipher_file, output):
    cipher = ""
    with open(key_file, "rb") as key_f:
        key = b""
        for i in key_f:
            key += i
    with open(cipher_file, "rb") as message_f:
        message = b""
        for t in message_f:
            message += t
    if len(message) > len(key):
        print("The key must be the same size or larger than the message.")
        exit()
    dec = open(output, 'wb')
    cipher = bytearray(len(message))
    for i in range(len(message)):   
        cipher[i] = (key[i]^message[i])     
    dec.write(cipher)
    dec.close()

if __name__ == "__main__":
    if len(argv) < 4:
        exit()
    Decrypt(argv[1], argv[2], argv[3])